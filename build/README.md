# CALL OF DUTY // HQ LAUNCHER - WINDOWS PC BUILD & RUNTIME MANIFEST

This folder contains the compiled standalone native Windows runtime artifacts for Call of Duty HQ.

## Bundled Artifacts

1. **`COD_HQ_Launcher.exe`** (77 KB)
   - **Architecture:** x86_64 (64-bit Windows PE Binary)
   - **Subsystem:** Windows GUI (`subsystem: windows`) - runs clean with zero command prompt flashing.
   - **Features:**
     * Per-Monitor V2 High-DPI scaling enabled (`SetProcessDpiAwarenessContext`)
     * Single instance mutex lock (`BringBackCODHQ_SingleInstance_Mutex`)
     * Automatic Python environment locator (checks `python/`, system PATH, AppData, Program Files)
     * Auto-boots Call of Duty HQ background server and launches standalone borderless app window via Microsoft Edge / Google Chrome (`--app=http://127.0.0.1:8000`).

2. **`cod_hq_bridge.dll`** (219 KB)
   - **Architecture:** x86_64 Windows Dynamic Link Library
   - **Exported Win32 Functions:**
     * `LaunchGameProcess(exePath, launchArgs, workingDir)`: Direct low-level process spawning with `CREATE_NEW_PROCESS_GROUP`.
     * `LaunchSteamUri(appId)`: Dispatches `steam://rungameid/<id>` protocol directly to the Windows Shell.
     * `LaunchBattleNetUri(productId)`: Dispatches `battlenet://<product>` protocol.
     * `OpenFolderInExplorer(folderPath)`: Opens folder in Windows File Explorer.
     * `IsProcessRunning(processName)`: Real-time process monitoring via Toolhelp32 snapshots.

3. **`COD_HQ_Launcher.bat`**
   - Instant double-click Windows command script that detects `pythonw.exe`, `py.exe`, or `python.exe` and launches the HQ in desktop mode.

4. **`COD_HQ.spec`**
   - Official PyInstaller specification file for compiling a 100% self-contained one-file or one-directory standalone binary package on Windows.

## How to Run on Windows PC

### Option A: Double-Click Native Executable
1. Double-click `COD_HQ_Launcher.exe`.
2. The launcher boots the HQ backend and displays the standalone military HUD interface.

### Option B: Batch Script
1. Double-click `COD_HQ_Launcher.bat`.

### Option C: Python Command Line
```powershell
python -m pip install -r requirements.txt
python main.py --desktop
```
