#!/usr/bin/env python3
"""Call of Duty HQ - Full Tactical PC Launcher.
Main application entry point. Serves the military HUD interface,
coordinates game auto-locating, Steam integration, and native Win32 process spawning.
"""

import os
import sys
import argparse
import webbrowser
import platform
import threading
import time
import uvicorn

from launcher.covers import generate_all_artwork
from launcher.server import app

def open_browser_delayed(url: str, delay: float = 1.0):
    """Open browser in desktop app mode after server starts."""
    time.sleep(delay)
    try:
        # On Windows, try Edge or Chrome app mode first
        if platform.system() == "Windows":
            import subprocess
            edge_cmd = f"msedge.exe --app={url} --window-size=1440,900"
            try:
                subprocess.Popen(edge_cmd, shell=True)
                return
            except Exception:
                pass
        webbrowser.open(url)
    except Exception:
        pass

def main():
    parser = argparse.ArgumentParser(description="Call of Duty HQ - Windows PC Tactical Launcher")
    parser.add_argument("--host", default="0.0.0.0", help="Host interface to bind (default: 0.0.0.0)")
    parser.add_argument("--port", type=int, default=8000, help="Port to listen on (default: 8000)")
    parser.add_argument("--desktop", action="store_true", help="Launch in desktop app window mode")
    parser.add_argument("--no-browser", action="store_true", help="Do not automatically open browser")
    args = parser.parse_args()

    print("=" * 65)
    print("   CALL OF DUTY // HQ - TACTICAL OPERATIONS PC LAUNCHER")
    print("=" * 65)
    print(f"[*] Initializing Franchise Codex & Artwork Cache...")
    generate_all_artwork()
    print(f"[+] 24 Franchise Titles Verified & Combat Ready.")
    print(f"[*] Starting Tactical HQ Server on http://{args.host}:{args.port}")

    if args.desktop and not args.no_browser:
        target_url = f"http://127.0.0.1:{args.port}"
        threading.Thread(target=open_browser_delayed, args=(target_url, 0.8), daemon=True).start()

    uvicorn.run(
        app,
        host=args.host,
        port=args.port,
        log_level="info",
        access_log=False
    )

if __name__ == "__main__":
    main()
