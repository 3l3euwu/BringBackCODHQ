/*
 * Call of Duty HQ - Windows Native Desktop Launcher
 * Entry point executable for Windows PCs.
 * Handles high-DPI scaling, background server bootstrap, and borderless app window launch.
 */

#define WIN32_LEAN_AND_MEAN
#include <windows.h>
#include <shellapi.h>
#include <winsock2.h>
#include <ws2tcpip.h>
#include <stdio.h>
#include <stdlib.h>

#pragma comment(lib, "ws2_32.lib")

// Set per-monitor DPI awareness if available on Windows 10/11
static void EnableDpiAwareness(void) {
    HMODULE hUser = LoadLibraryA("user32.dll");
    if (hUser) {
        typedef BOOL (WINAPI *SetProcessDpiAwarenessContextProc)(HANDLE);
        SetProcessDpiAwarenessContextProc pSet = (SetProcessDpiAwarenessContextProc)GetProcAddress(hUser, "SetProcessDpiAwarenessContext");
        if (pSet) {
            // -4 = DPI_AWARENESS_CONTEXT_PER_MONITOR_AWARE_V2
            pSet((HANDLE)-4);
        }
        FreeLibrary(hUser);
    }
}

// Check if TCP port 8000 is accepting connections
static BOOL IsPortOpen(int port) {
    WSADATA wsa;
    if (WSAStartup(MAKEWORD(2, 2), &wsa) != 0) return FALSE;

    SOCKET s = socket(AF_INET, SOCK_STREAM, IPPROTO_TCP);
    if (s == INVALID_SOCKET) {
        WSACleanup();
        return FALSE;
    }

    struct sockaddr_in addr;
    addr.sin_family = AF_INET;
    addr.sin_port = htons((u_short)port);
    addr.sin_addr.s_addr = inet_addr("127.0.0.1");

    u_long mode = 1;
    ioctlsocket(s, FIONBIO, &mode);

    connect(s, (struct sockaddr*)&addr, sizeof(addr));

    fd_set writes;
    FD_ZERO(&writes);
    FD_SET(s, &writes);

    struct timeval tv;
    tv.tv_sec = 0;
    tv.tv_usec = 200000; // 200ms

    BOOL isOpen = FALSE;
    if (select(0, NULL, &writes, NULL, &tv) > 0) {
        isOpen = TRUE;
    }

    closesocket(s);
    WSACleanup();
    return isOpen;
}

// Find Python executable on Windows
static BOOL FindPython(char* outPath, size_t maxLen) {
    // 1. Check local bundled python directory
    if (GetFileAttributesA("python\\pythonw.exe") != INVALID_FILE_ATTRIBUTES) {
        strncpy(outPath, "python\\pythonw.exe", maxLen);
        return TRUE;
    }
    if (GetFileAttributesA("..\\python\\pythonw.exe") != INVALID_FILE_ATTRIBUTES) {
        strncpy(outPath, "..\\python\\pythonw.exe", maxLen);
        return TRUE;
    }
    if (GetFileAttributesA("python\\python.exe") != INVALID_FILE_ATTRIBUTES) {
        strncpy(outPath, "python\\python.exe", maxLen);
        return TRUE;
    }

    // 2. Check Windows py launcher or pythonw.exe in PATH
    char searchBuf[MAX_PATH];
    if (SearchPathA(NULL, "pythonw.exe", NULL, MAX_PATH, searchBuf, NULL)) {
        strncpy(outPath, searchBuf, maxLen);
        return TRUE;
    }
    if (SearchPathA(NULL, "py.exe", NULL, MAX_PATH, searchBuf, NULL)) {
        strncpy(outPath, searchBuf, maxLen);
        return TRUE;
    }
    if (SearchPathA(NULL, "python.exe", NULL, MAX_PATH, searchBuf, NULL)) {
        strncpy(outPath, searchBuf, maxLen);
        return TRUE;
    }

    // 3. Check AppData local programs python
    char localAppData[MAX_PATH];
    if (GetEnvironmentVariableA("LOCALAPPDATA", localAppData, MAX_PATH)) {
        char pyTest[MAX_PATH];
        for (int v = 14; v >= 10; v--) {
            wsprintfA(pyTest, "%s\\Programs\\Python\\Python3%d\\pythonw.exe", localAppData, v);
            if (GetFileAttributesA(pyTest) != INVALID_FILE_ATTRIBUTES) {
                strncpy(outPath, pyTest, maxLen);
                return TRUE;
            }
        }
    }

    return FALSE;
}

// Launch borderless desktop app view using Edge or Chrome in app mode
static void LaunchAppWindow(const char* url) {
    char cmd[1024];

    // 1. Try Microsoft Edge in standalone --app mode
    char edgePath[MAX_PATH];
    BOOL hasEdge = FALSE;
    if (SearchPathA(NULL, "msedge.exe", NULL, MAX_PATH, edgePath, NULL)) {
        hasEdge = TRUE;
    } else {
        const char* standardEdge = "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe";
        if (GetFileAttributesA(standardEdge) != INVALID_FILE_ATTRIBUTES) {
            strncpy(edgePath, standardEdge, MAX_PATH);
            hasEdge = TRUE;
        }
    }

    if (hasEdge) {
        wsprintfA(cmd, "\"%s\" --app=%s --window-size=1440,900", edgePath, url);
        STARTUPINFOA si = { sizeof(si) };
        PROCESS_INFORMATION pi;
        if (CreateProcessA(NULL, cmd, NULL, NULL, FALSE, 0, NULL, NULL, &si, &pi)) {
            CloseHandle(pi.hProcess);
            CloseHandle(pi.hThread);
            return;
        }
    }

    // 2. Try Chrome in app mode
    char chromePath[MAX_PATH];
    if (SearchPathA(NULL, "chrome.exe", NULL, MAX_PATH, chromePath, NULL)) {
        wsprintfA(cmd, "\"%s\" --app=%s --window-size=1440,900", chromePath, url);
        STARTUPINFOA si = { sizeof(si) };
        PROCESS_INFORMATION pi;
        if (CreateProcessA(NULL, cmd, NULL, NULL, FALSE, 0, NULL, NULL, &si, &pi)) {
            CloseHandle(pi.hProcess);
            CloseHandle(pi.hThread);
            return;
        }
    }

    // 3. Fallback: ShellExecute default browser
    ShellExecuteA(NULL, "open", url, NULL, NULL, SW_SHOWNORMAL);
}

int WINAPI WinMain(HINSTANCE hInstance, HINSTANCE hPrevInstance, LPSTR lpCmdLine, int nCmdShow) {
    EnableDpiAwareness();

    // Prevent multiple instances
    HANDLE hMutex = CreateMutexA(NULL, TRUE, "BringBackCODHQ_SingleInstance_Mutex");
    if (GetLastError() == ERROR_ALREADY_EXISTS) {
        LaunchAppWindow("http://127.0.0.1:8000");
        return 0;
    }

    int port = 8000;
    char targetUrl[128];
    wsprintfA(targetUrl, "http://127.0.0.1:%d", port);

    // If server is not already running, spawn it
    if (!IsPortOpen(port)) {
        char pythonPath[MAX_PATH];
        if (!FindPython(pythonPath, sizeof(pythonPath))) {
            int res = MessageBoxA(
                NULL,
                "Call of Duty HQ Launcher requires Python 3.10+ runtime.\n\n"
                "Would you like to visit Python.org to download it now?",
                "CALL OF DUTY // HQ BOOTLOADER",
                MB_YESNO | MB_ICONWARNING
            );
            if (res == IDYES) {
                ShellExecuteA(NULL, "open", "https://www.python.org/downloads/", NULL, NULL, SW_SHOWNORMAL);
            }
            return 1;
        }

        // Determine working directory (parent of build, or current dir)
        char workingDir[MAX_PATH] = ".";
        if (GetFileAttributesA("main.py") == INVALID_FILE_ATTRIBUTES) {
            if (GetFileAttributesA("..\\main.py") != INVALID_FILE_ATTRIBUTES) {
                strcpy(workingDir, "..");
            }
        }

        char serverCmd[2048];
        wsprintfA(serverCmd, "\"%s\" \"%s\\main.py\" --desktop --port %d", pythonPath, workingDir, port);

        STARTUPINFOA si;
        PROCESS_INFORMATION pi;
        ZeroMemory(&si, sizeof(si));
        si.cb = sizeof(si);
        ZeroMemory(&pi, sizeof(pi));

        // Start in background without black console
        BOOL started = CreateProcessA(
            NULL,
            serverCmd,
            NULL,
            NULL,
            FALSE,
            CREATE_NO_WINDOW,
            NULL,
            workingDir,
            &si,
            &pi
        );

        if (!started) {
            MessageBoxA(NULL, "Failed to initialize Call of Duty HQ server process.", "COD HQ // ERROR", MB_OK | MB_ICONERROR);
            return 1;
        }

        CloseHandle(pi.hProcess);
        CloseHandle(pi.hThread);

        // Wait for port to open
        for (int i = 0; i < 25; i++) {
            Sleep(200);
            if (IsPortOpen(port)) break;
        }
    }

    // Launch UI
    LaunchAppWindow(targetUrl);

    if (hMutex) CloseHandle(hMutex);
    return 0;
}
