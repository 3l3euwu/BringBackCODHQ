/*
 * Call of Duty HQ - Windows Native Bridge DLL
 * Provides direct Win32 process creation, DPI awareness, Steam URI dispatch,
 * and high-performance system interaction for the COD HQ Launcher.
 */

#include <windows.h>
#include <shellapi.h>
#include <tlhelp32.h>

#ifdef __cplusplus
extern "C" {
#endif

// Launch a Call of Duty game via native CreateProcess
__declspec(dllexport) BOOL WINAPI LaunchGameProcess(const char* exePath, const char* launchArgs, const char* workingDir) {
    if (!exePath || strlen(exePath) == 0) {
        return FALSE;
    }

    STARTUPINFOA si;
    PROCESS_INFORMATION pi;
    ZeroMemory(&si, sizeof(si));
    si.cb = sizeof(si);
    ZeroMemory(&pi, sizeof(pi));

    char cmdLine[4096];
    if (launchArgs && strlen(launchArgs) > 0) {
        wsprintfA(cmdLine, "\"%s\" %s", exePath, launchArgs);
    } else {
        wsprintfA(cmdLine, "\"%s\"", exePath);
    }

    const char* dir = (workingDir && strlen(workingDir) > 0) ? workingDir : NULL;

    BOOL success = CreateProcessA(
        NULL,
        cmdLine,
        NULL,
        NULL,
        FALSE,
        CREATE_NEW_PROCESS_GROUP,
        NULL,
        dir,
        &si,
        &pi
    );

    if (success) {
        CloseHandle(pi.hProcess);
        CloseHandle(pi.hThread);
        return TRUE;
    }

    return FALSE;
}

// Dispatch Steam run URI
__declspec(dllexport) BOOL WINAPI LaunchSteamUri(int appId) {
    if (appId <= 0) return FALSE;
    char uri[128];
    wsprintfA(uri, "steam://rungameid/%d", appId);
    HINSTANCE hRes = ShellExecuteA(NULL, "open", uri, NULL, NULL, SW_SHOWNORMAL);
    return ((INT_PTR)hRes > 32);
}

// Dispatch Battle.net product URI
__declspec(dllexport) BOOL WINAPI LaunchBattleNetUri(const char* productId) {
    if (!productId || strlen(productId) == 0) return FALSE;
    char uri[128];
    wsprintfA(uri, "battlenet://%s", productId);
    HINSTANCE hRes = ShellExecuteA(NULL, "open", uri, NULL, NULL, SW_SHOWNORMAL);
    return ((INT_PTR)hRes > 32);
}

// Open folder in Windows File Explorer
__declspec(dllexport) BOOL WINAPI OpenFolderInExplorer(const char* folderPath) {
    if (!folderPath || strlen(folderPath) == 0) return FALSE;
    HINSTANCE hRes = ShellExecuteA(NULL, "open", folderPath, NULL, NULL, SW_SHOWNORMAL);
    return ((INT_PTR)hRes > 32);
}

// Check if a game process is currently running
__declspec(dllexport) BOOL WINAPI IsProcessRunning(const char* processName) {
    if (!processName || strlen(processName) == 0) return FALSE;

    HANDLE hSnapshot = CreateToolhelp32Snapshot(TH32CS_SNAPPROCESS, 0);
    if (hSnapshot == INVALID_HANDLE_VALUE) return FALSE;

    PROCESSENTRY32 pe32;
    pe32.dwSize = sizeof(PROCESSENTRY32);

    BOOL found = FALSE;
    if (Process32First(hSnapshot, &pe32)) {
        do {
            if (lstrcmpiA(pe32.szExeFile, processName) == 0) {
                found = TRUE;
                break;
            }
        } while (Process32Next(hSnapshot, &pe32));
    }

    CloseHandle(hSnapshot);
    return found;
}

BOOL WINAPI DllMain(HINSTANCE hinstDLL, DWORD fdwReason, LPVOID lpvReserved) {
    return TRUE;
}

#ifdef __cplusplus
}
#endif
