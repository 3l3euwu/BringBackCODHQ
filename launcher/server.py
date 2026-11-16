"""FastAPI Server for Call of Duty HQ Launcher.
Serves the tactical military desktop interface and handles REST APIs for
game launching, PC auto-locating, Steam sync, and custom cover management.
"""

import os
from pathlib import Path
from typing import Dict, Any, Optional, List
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from launcher.database import (
    GAMES_DATABASE,
    get_all_games,
    get_game_by_id
)
from launcher.scanner import scan_pc_for_games, apply_detected_games
from launcher.steam import (
    get_current_profile,
    fetch_steam_web_profile,
    sync_achievements_for_game
)
from launcher.bridge import launch_game, open_game_folder
from launcher.covers import fetch_or_create_artwork, generate_tactical_cover

BASE_DIR = Path(__file__).parent.parent
UI_DIR = BASE_DIR / "ui"
ASSETS_DIR = BASE_DIR / "assets"

app = FastAPI(
    title="Call of Duty HQ - Tactical Launcher",
    version="1.0.0",
    docs_url=None,
    redoc_url=None
)

# Enable CORS for preview environment
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount static asset folders
app.mount("/ui", StaticFiles(directory=str(UI_DIR)), name="ui")
app.mount("/assets", StaticFiles(directory=str(ASSETS_DIR)), name="assets")


# Request Models
class LaunchRequest(BaseModel):
    mode: Optional[str] = "default"
    custom_args: Optional[str] = None


class GameUpdateRequest(BaseModel):
    installed_path: Optional[str] = None
    launch_args: Optional[str] = None
    is_installed: Optional[bool] = None
    is_favorite: Optional[bool] = None


class CoverRequest(BaseModel):
    image_url: Optional[str] = None


class ScanRequest(BaseModel):
    custom_dirs: Optional[List[str]] = None


class ApplyScanRequest(BaseModel):
    detected_games: List[Dict[str, Any]]


class SteamSyncRequest(BaseModel):
    steam_id: Optional[str] = None
    api_key: Optional[str] = None


# Routes
@app.get("/")
@app.head("/")
async def serve_index():
    index_path = UI_DIR / "index.html"
    return FileResponse(str(index_path))


@app.get("/api/games")
async def list_games():
    """List all Call of Duty franchise titles with status and playtime."""
    return get_all_games()


@app.get("/api/games/{game_id}")
async def get_game(game_id: str):
    """Retrieve full intel dossier for a specific Call of Duty release."""
    game = get_game_by_id(game_id)
    if not game:
        raise HTTPException(status_code=404, detail="Game not found")
    return game


@app.post("/api/games/{game_id}/launch")
async def execute_launch(game_id: str, req: LaunchRequest):
    """Deploy / launch a Call of Duty game."""
    game = get_game_by_id(game_id)
    if not game:
        raise HTTPException(status_code=404, detail="Game not found")

    result = launch_game(game, custom_args=req.custom_args, launch_mode=req.mode or "default")
    return result


@app.post("/api/games/{game_id}/update")
async def update_game_config(game_id: str, req: GameUpdateRequest):
    """Update install path, launch parameters, or status."""
    game = get_game_by_id(game_id)
    if not game:
        raise HTTPException(status_code=404, detail="Game not found")

    if req.installed_path is not None:
        game["installed_path"] = req.installed_path.strip()
    if req.launch_args is not None:
        game["launch_args"] = req.launch_args.strip()
    if req.is_installed is not None:
        game["is_installed"] = req.is_installed
    if req.is_favorite is not None:
        game["is_favorite"] = req.is_favorite

    return {"success": True, "game": game}


@app.post("/api/games/{game_id}/folder")
async def open_folder(game_id: str):
    """Open game directory in Windows Explorer or system file manager."""
    game = get_game_by_id(game_id)
    if not game:
        raise HTTPException(status_code=404, detail="Game not found")

    return open_game_folder(game)


@app.post("/api/games/{game_id}/cover")
async def update_cover(game_id: str, req: CoverRequest):
    """Change game cover art from URL or reset to procedural tactical art."""
    game = get_game_by_id(game_id)
    if not game:
        raise HTTPException(status_code=404, detail="Game not found")

    cover_file = ASSETS_DIR / "covers" / f"{game_id}.jpg"

    if req.image_url:
        try:
            import requests
            from PIL import Image
            import io
            res = requests.get(req.image_url, timeout=5)
            if res.status_code == 200:
                img = Image.open(io.BytesIO(res.content)).convert("RGB")
                img = img.resize((600, 900), Image.LANCZOS)
                img.save(cover_file, "JPEG", quality=90)
                return {"success": True, "message": "Custom cover downloaded and applied."}
        except Exception as e:
            pass

    # Reset / generate procedural
    generate_tactical_cover(game, cover_file)
    return {"success": True, "message": "Cover reset to high-res tactical artwork."}


@app.post("/api/scan")
async def scan_pc(req: Optional[ScanRequest] = None):
    """Deep scan PC drives for Call of Duty installations."""
    custom_dirs = req.custom_dirs if req else None
    results = scan_pc_for_games(custom_dirs)
    return results


@app.post("/api/scan/apply")
async def apply_scan(req: ApplyScanRequest):
    """Apply auto-detected game paths to library."""
    count = apply_detected_games(req.detected_games)
    return {"success": True, "applied_count": count}


@app.get("/api/steam/profile")
async def get_steam_profile():
    """Retrieve active Steam operator profile and franchise combat record."""
    return get_current_profile()


@app.post("/api/steam/sync")
async def sync_steam(req: SteamSyncRequest):
    """Synchronize with Steam ID or Web API."""
    profile = fetch_steam_web_profile(req.steam_id or "76561198141022141", req.api_key)
    return {"success": True, "profile": profile}


@app.get("/api/steam/achievements/{game_id}")
async def get_achievements(game_id: str, steam_id: Optional[str] = "76561198141022141"):
    """Fetch achievements ('succès') for specific title."""
    return sync_achievements_for_game(game_id, steam_id)
