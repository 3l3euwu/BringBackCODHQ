# CALL OF DUTY // HQ - TACTICAL PC LAUNCHER

> **A full-featured standalone Call of Duty HQ desktop launcher for Windows PCs.**
> Built with Python, native Win32 C/C++ bridge DLLs, and a tactical military/camo/sand HUD aesthetic.

![COD HQ Icon](assets/icons/cod_hq.png)

---

## Key Features

- **Exhaustive Franchise Database:**
  Complete catalog of all 27 mainline Call of Duty releases from the 2003 original to *Call of Duty: Black Ops 6*, *Call of Duty: Black Ops 7*, and *Call of Duty: Modern Warfare 4*, including the *Modern Warfare* saga, *Black Ops*, *World War II*, *Warzone*, and Classic eras.
- **Modern Tactical Military UI:**
  - Modern Warfare / Warzone inspired aesthetic: Dark Charcoal, Tactical Olive Drab, Camo overlays, and Desert Sand / Khaki highlights.
  - Three switchable military themes: **Tactical Olive Drab**, **Desert Sand & Khaki**, and **Night Ops Stealth Camo**.
  - Built-in tactical audio synthesizer (Web Audio API) delivering military mechanical clicks, deployment pulses, and radar chirps.
- **Dynamic Cover Art & Hero Banners:**
  - Automatically fetches official 600x900 library covers from Steam CDN when network is available.
  - Bundled offline procedural cover art generator (using Pillow) creates military-grade tactical box art and 1080p hero banners for every game.
  - Support for custom cover art uploading and changing.
- **Deep PC Game Auto-Locator:**
  - Scans Steam libraries across all storage drives via `libraryfolders.vdf` and `appmanifest_*.acf`.
  - Scans Battle.net agent paths and standard Activision directories (`ModernWarfare.exe`, `BlackOpsColdWar.exe`, `Vanguard.exe`, `cod.exe`).
  - Scans Xbox App / PC Game Pass directories.
  - Supports custom drive and directory scanning with an animated radar HUD.
- **Steam Integration (Local & Web API):**
  - Reads local Steam client files (`loginusers.vdf`, `config.vdf`) to detect active Steam user without logging in.
  - Supports SteamID64 / Steam Web API key synchronization to pull live playtime and achievements ("succès").
  - Includes offline "Operator Ghost 141" combat record profile for testing without a Steam connection.
  - Achievements inspector with completion bars, medal icons, and status tracking for every game.
- **Autonomous Windows Executable Bundle in `build/`:**
  - `build/COD_HQ_Launcher.exe`: Native 64-bit Windows GUI Subsystem executable (Per-Monitor V2 High-DPI aware, background server supervisor, borderless window launcher).
  - `build/cod_hq_bridge.dll`: Win32 native bridge DLL exporting direct process execution (`LaunchGameProcess`), Steam protocol dispatch (`LaunchSteamUri`), and file explorer hooks.
  - `build/COD_HQ_Launcher.bat`: Instant double-click Windows script.
  - `build/COD_HQ.spec`: PyInstaller spec file for self-contained packaging.

---

## Repository Structure

```
BringBackCODHQ/
├── assets/
│   ├── covers/            # 600x900 Box art covers for every COD title
│   ├── banners/           # 1920x1080 Cinematic hero banners
│   └── icons/             # COD HQ insignia (.png & .ico)
├── build/
│   ├── COD_HQ_Launcher.exe # Native Windows 64-bit GUI executable (77 KB)
│   ├── cod_hq_bridge.dll   # Win32 native process & Steam bridge DLL (219 KB)
│   ├── COD_HQ_Launcher.bat # Windows batch bootstrap script
│   ├── COD_HQ.spec        # PyInstaller specification file
│   ├── launcher.c         # C source for Windows GUI launcher
│   ├── cod_hq_bridge.c    # C source for native bridge DLL
│   └── README.md          # Build & runtime documentation
├── launcher/
│   ├── __init__.py
│   ├── database.py        # 24+ Call of Duty games database with specs & achievements
│   ├── covers.py          # Steam CDN fetcher & procedural tactical art generator
│   ├── scanner.py         # PC game auto-locator for Steam, Battle.net, Xbox
│   ├── steam.py           # Steam VDF reader, profile sync, achievements parser
│   ├── bridge.py          # Native ctypes bridge & process dispatcher
│   └── server.py          # FastAPI REST API & static file server
├── ui/
│   ├── index.html         # Modern tactical military HUD interface
│   ├── style.css          # Military green/camo/sand styling, radar HUD, responsive design
│   └── app.js             # Client controller, Web Audio synthesizer, live filters
├── main.py                # Top-level application entry point
├── requirements.txt       # Python dependencies
└── README.md
```

---

## Running Call of Duty HQ

### Live Web / Desktop Mode (Linux / Mac / Windows)
```bash
python3 main.py --host 0.0.0.0 --port 8000
```
Then navigate to `http://localhost:8000` in your web browser.

### Windows Desktop Executable
Navigate to the `build/` folder and double-click:
- `COD_HQ_Launcher.exe`
or
- `COD_HQ_Launcher.bat`

---

## Franchise Games Covered

1. Call of Duty (2003)
2. Call of Duty: United Offensive (2004)
3. Call of Duty 2 (2005)
4. Call of Duty 3 (2006)
5. Call of Duty 4: Modern Warfare (2007)
6. Call of Duty: World at War (2008)
7. Call of Duty: Modern Warfare 2 (2009)
8. Call of Duty: Black Ops (2010)
9. Call of Duty: Modern Warfare 3 (2011)
10. Call of Duty: Black Ops II (2012)
11. Call of Duty: Ghosts (2013)
12. Call of Duty: Advanced Warfare (2014)
13. Call of Duty: Black Ops III (2015)
14. Call of Duty: Infinite Warfare (2016)
15. Call of Duty: Modern Warfare Remastered (2016)
16. Call of Duty: WWII (2017)
17. Call of Duty: Black Ops 4 (2018)
18. Call of Duty: Modern Warfare (2019)
19. Call of Duty: Warzone (2020)
20. Call of Duty: Modern Warfare 2 Campaign Remastered (2020)
21. Call of Duty: Black Ops Cold War (2020)
22. Call of Duty: Vanguard (2021)
23. Call of Duty: Modern Warfare II (2022)
24. Call of Duty: Modern Warfare III (2023)
25. Call of Duty: Black Ops 6 (2024)
26. Call of Duty: Black Ops 7 (2025/2026 - Project Endgame)
27. Call of Duty: Modern Warfare 4 (2026 - Task Force 141 Final Strike)
