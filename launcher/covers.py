"""Cover art and banner management for Call of Duty HQ.
Fetches high-res official covers from Steam CDN when accessible,
and procedurally generates tactical, military-grade artwork for all games.
"""

import os
import math
import random
from pathlib import Path
from typing import Dict, Any, Tuple
import requests
from PIL import Image, ImageDraw, ImageFont, ImageFilter

ASSETS_DIR = Path(__file__).parent.parent / "assets"
COVERS_DIR = ASSETS_DIR / "covers"
BANNERS_DIR = ASSETS_DIR / "banners"

COVERS_DIR.mkdir(parents=True, exist_ok=True)
BANNERS_DIR.mkdir(parents=True, exist_ok=True)

SERIES_THEMES: Dict[str, Dict[str, Any]] = {
    "Modern Warfare": {
        "bg_top": (10, 16, 12),
        "bg_bot": (18, 28, 20),
        "accent": (74, 222, 128),      # Tactical Night-Vision Green
        "accent_dim": (34, 84, 48),
        "gold": (212, 178, 111),       # Desert Sand
        "tag": "TASK FORCE 141 // GOING DARK",
        "symbol": "MW"
    },
    "Black Ops": {
        "bg_top": (18, 12, 10),
        "bg_bot": (28, 16, 14),
        "accent": (249, 115, 22),       # Tactical Classified Orange
        "accent_dim": (124, 45, 18),
        "gold": (224, 182, 104),
        "tag": "CLASSIFIED // SOG PROTOCOL",
        "symbol": "BO"
    },
    "World War II": {
        "bg_top": (16, 18, 14),
        "bg_bot": (24, 26, 18),
        "accent": (217, 180, 110),      # Vintage Sand Khaki
        "accent_dim": (80, 70, 45),
        "gold": (230, 200, 130),
        "tag": "INFANTRY DIVISION // NORMANDY TO RHINE",
        "symbol": "WWII"
    },
    "Advanced & Futuristic": {
        "bg_top": (10, 14, 22),
        "bg_bot": (16, 24, 34),
        "accent": (56, 189, 248),       # Cyber / Exo Cyan
        "accent_dim": (20, 60, 90),
        "gold": (234, 179, 8),
        "tag": "EXO PROTOCOL // SOLAR DEFENSE",
        "symbol": "EXO"
    },
    "Warzone": {
        "bg_top": (14, 14, 12),
        "bg_bot": (22, 22, 18),
        "accent": (234, 179, 8),        # High-Alert Hazard Yellow
        "accent_dim": (100, 75, 15),
        "gold": (212, 178, 111),
        "tag": "RESURGENCE // SQUAD DROP",
        "symbol": "WZ"
    },
    "Classic Era": {
        "bg_top": (18, 18, 14),
        "bg_bot": (28, 26, 20),
        "accent": (202, 168, 104),      # Classic Khaki
        "accent_dim": (75, 65, 42),
        "gold": (230, 205, 140),
        "tag": "ORIGINAL BATTLEFIELDS // 2003-2006",
        "symbol": "COD"
    }
}

def _draw_tactical_grid(draw: ImageDraw.ImageDraw, width: int, height: int, color: Tuple[int, int, int, int], step: int = 40):
    for x in range(0, width, step):
        draw.line([(x, 0), (x, height)], fill=color, width=1)
    for y in range(0, height, step):
        draw.line([(0, y), (width, y)], fill=color, width=1)

def _draw_corner_brackets(draw: ImageDraw.ImageDraw, x1: int, y1: int, x2: int, y2: int, color: Tuple[int, int, int], length: int = 24, thickness: int = 2):
    # Top-Left
    draw.line([(x1, y1), (x1 + length, y1)], fill=color, width=thickness)
    draw.line([(x1, y1), (x1, y1 + length)], fill=color, width=thickness)
    # Top-Right
    draw.line([(x2 - length, y1), (x2, y1)], fill=color, width=thickness)
    draw.line([(x2, y1), (x2, y1 + length)], fill=color, width=thickness)
    # Bottom-Left
    draw.line([(x1, y2 - length), (x1, y2)], fill=color, width=thickness)
    draw.line([(x1, y2), (x1 + length, y2)], fill=color, width=thickness)
    # Bottom-Right
    draw.line([(x2 - length, y2), (x2, y2)], fill=color, width=thickness)
    draw.line([(x2, y2 - length), (x2, y2)], fill=color, width=thickness)

def generate_tactical_cover(game: Dict[str, Any], output_path: Path):
    """Generate high-resolution 600x900 military cover art for a Call of Duty game."""
    width, height = 600, 900
    im = Image.new("RGB", (width, height))
    draw = ImageDraw.Draw(im)

    series = game.get("series", "Modern Warfare")
    theme = SERIES_THEMES.get(series, SERIES_THEMES["Modern Warfare"])

    # 1. Background gradient
    c_top = theme["bg_top"]
    c_bot = theme["bg_bot"]
    for y in range(height):
        ratio = y / height
        r = int(c_top[0] * (1 - ratio) + c_bot[0] * ratio)
        g = int(c_top[1] * (1 - ratio) + c_bot[1] * ratio)
        b = int(c_top[2] * (1 - ratio) + c_bot[2] * ratio)
        draw.line([(0, y), (width, y)], fill=(r, g, b))

    # 2. Subtle tactical grid overlay
    overlay = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    ov_draw = ImageDraw.Draw(overlay)
    _draw_tactical_grid(ov_draw, width, height, (255, 255, 255, 10), step=35)
    
    # 3. Geometric Camo / Military Polygon Accents
    random.seed(sum(ord(c) for c in game["id"]))
    accent_rgb = theme["accent"]
    for _ in range(8):
        px = random.randint(30, width - 30)
        py = random.randint(150, height - 250)
        size = random.randint(40, 120)
        poly = [
            (px, py),
            (px + size, py + random.randint(-20, 20)),
            (px + size + random.randint(-20, 30), py + size),
            (px + random.randint(-10, 20), py + size + random.randint(-15, 15))
        ]
        ov_draw.polygon(poly, fill=(accent_rgb[0], accent_rgb[1], accent_rgb[2], 12))

    im.paste(Image.alpha_composite(im.convert("RGBA"), overlay).convert("RGB"))
    draw = ImageDraw.Draw(im)

    # 4. Tactical Outer Borders & Corner Brackets
    border_color = theme["accent_dim"]
    draw.rectangle([(16, 16), (width - 16, height - 16)], outline=border_color, width=2)
    draw.rectangle([(22, 22), (width - 22, height - 22)], outline=(35, 45, 38), width=1)
    _draw_corner_brackets(draw, 12, 12, width - 12, height - 12, theme["accent"], length=32, thickness=3)

    # 5. Top Header Stencil Bar
    draw.rectangle([(24, 24), (width - 24, 56)], fill=(12, 16, 14))
    draw.line([(24, 56), (width - 24, 56)], fill=theme["accent"], width=2)
    
    # Header text
    header_text = f"CALL OF DUTY // HQ INTEL [{game.get('release_year', 'CLASSIFIED')}]"
    draw.text((36, 32), header_text, fill=theme["gold"])
    
    # Status indicator LED
    led_color = (74, 222, 128) if game.get("is_installed") else (156, 163, 175)
    draw.ellipse([(width - 50, 34), (width - 38, 46)], fill=led_color)

    # 6. Central Emblem / Big Military Graphics
    cy = 380
    # Outer target ring
    draw.ellipse([(width//2 - 140, cy - 140), (width//2 + 140, cy + 140)], outline=(theme["accent_dim"]), width=2)
    draw.ellipse([(width//2 - 110, cy - 110), (width//2 + 110, cy + 110)], outline=(theme["accent"][0]//2, theme["accent"][1]//2, theme["accent"][2]//2), width=1)
    
    # Crosshair lines
    draw.line([(width//2 - 170, cy), (width//2 - 120, cy)], fill=theme["accent"], width=2)
    draw.line([(width//2 + 120, cy), (width//2 + 170, cy)], fill=theme["accent"], width=2)
    draw.line([(width//2, cy - 170), (width//2, cy - 120)], fill=theme["accent"], width=2)
    draw.line([(width//2, cy + 120), (width//2, cy + 170)], fill=theme["accent"], width=2)

    # Big Series Emblem
    symbol = theme["symbol"]
    try:
        # Fallback to default font
        font_large = ImageFont.load_default()
    except Exception:
        font_large = None

    # Big insignia badge
    badge_rect = [(width//2 - 85, cy - 45), (width//2 + 85, cy + 45)]
    draw.rectangle(badge_rect, fill=(16, 22, 18), outline=theme["accent"], width=2)
    draw.text((width//2 - 40, cy - 15), f"[ {symbol} ]", fill=theme["accent"])

    # Tactical callout tag
    draw.text((width//2 - 100, cy + 80), theme["tag"], fill=(160, 175, 165))

    # 7. Lower Section: Title Banner with Tactical Shading
    draw.rectangle([(24, height - 260), (width - 24, height - 60)], fill=(12, 18, 14))
    draw.line([(24, height - 260), (width - 24, height - 260)], fill=theme["accent"], width=2)

    # Franchises Brand Header
    draw.text((42, height - 245), "ACTIVISION // TACTICAL ARCHIVE", fill=theme["gold"])

    # Game Title Lines
    title = game["title"]
    # Break title into clean lines if long
    if ":" in title:
        parts = title.split(":", 1)
        main_t = parts[0].strip().upper()
        sub_t = parts[1].strip().upper()
    else:
        main_t = title.upper()
        sub_t = game.get("subtitle", "").upper()

    draw.text((42, height - 215), main_t, fill=(245, 245, 240))
    if sub_t:
        draw.text((42, height - 185), sub_t[:45], fill=theme["accent"])

    # Specs / Metadata row
    dev_text = f"DEV: {game.get('developer', 'Infinity Ward').upper()[:28]}"
    draw.text((42, height - 145), dev_text, fill=(180, 190, 180))
    
    eng_text = f"ENGINE: {game.get('engine', 'IW Engine').upper()[:28]}"
    draw.text((42, height - 125), eng_text, fill=(140, 150, 140))

    modes_text = "MODES: " + " | ".join(game.get("modes", ["Campaign", "Multiplayer"])[:3]).upper()
    draw.text((42, height - 100), modes_text[:50], fill=theme["gold"])

    # 8. Bottom Bar: Rating / Status
    draw.rectangle([(24, height - 50), (width - 24, height - 24)], fill=(8, 12, 10))
    status_label = "STATUS: DEPLOYED // READY" if game.get("is_installed") else "STATUS: AVAILABLE // UNINSTALLED"
    draw.text((36, height - 42), status_label, fill=theme["accent"])
    draw.text((width - 120, height - 42), "RATING: [ M ]", fill=theme["gold"])

    output_path.parent.mkdir(parents=True, exist_ok=True)
    im.save(output_path, "JPEG", quality=90)


def generate_tactical_banner(game: Dict[str, Any], output_path: Path):
    """Generate high-resolution 1920x1080 cinematic hero banner for game detail view."""
    width, height = 1920, 1080
    im = Image.new("RGB", (width, height))
    draw = ImageDraw.Draw(im)

    series = game.get("series", "Modern Warfare")
    theme = SERIES_THEMES.get(series, SERIES_THEMES["Modern Warfare"])

    # 1. Dark atmospheric cinematic gradient
    c_top = theme["bg_top"]
    c_bot = theme["bg_bot"]
    for y in range(height):
        ratio = y / height
        r = int(c_top[0] * (1 - ratio) + c_bot[0] * ratio)
        g = int(c_top[1] * (1 - ratio) + c_bot[1] * ratio)
        b = int(c_top[2] * (1 - ratio) + c_bot[2] * ratio)
        draw.line([(0, y), (width, y)], fill=(r, g, b))

    # 2. Tactical grid and combat radar overlay
    overlay = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    ov_draw = ImageDraw.Draw(overlay)
    _draw_tactical_grid(ov_draw, width, height, (255, 255, 255, 12), step=60)

    # Large radar circles on right side
    rcx, rcy = width - 420, height // 2
    for r in [120, 240, 360, 480]:
        ov_draw.ellipse([(rcx - r, rcy - r), (rcx + r, rcy + r)], outline=(theme["accent"][0], theme["accent"][1], theme["accent"][2], 30), width=2)
    ov_draw.line([(rcx - 520, rcy), (rcx + 520, rcy)], fill=(theme["accent"][0], theme["accent"][1], theme["accent"][2], 40), width=1)
    ov_draw.line([(rcx, rcy - 520), (rcx, rcy + 520)], fill=(theme["accent"][0], theme["accent"][1], theme["accent"][2], 40), width=1)

    # Radar sweep line
    ov_draw.line([(rcx, rcy), (rcx + 340, rcy - 200)], fill=(theme["accent"][0], theme["accent"][1], theme["accent"][2], 120), width=3)

    im.paste(Image.alpha_composite(im.convert("RGBA"), overlay).convert("RGB"))
    draw = ImageDraw.Draw(im)

    # 3. Vignette (Dark edges)
    draw.rectangle([(0, 0), (width, 80)], fill=(0, 0, 0))
    draw.rectangle([(0, height - 160), (width, height)], fill=(0, 0, 0))

    # 4. Corner tactical markers
    _draw_corner_brackets(draw, 40, 40, width - 40, height - 40, theme["accent"], length=60, thickness=3)

    # 5. Header HUD info
    draw.text((60, 48), f"HQ RADAR SATELLITE LINK // SECTOR: {series.upper()}", fill=theme["accent"])
    draw.text((width - 380, 48), f"FREQ: 141.22 MHz // SYS: ONLINE", fill=theme["gold"])

    # 6. Prominent Tactical Hero Titles
    draw.text((80, height // 2 - 120), "CALL OF DUTY // COMBAT DOSSIER", fill=theme["gold"])
    draw.text((80, height // 2 - 70), game["title"].upper(), fill=(255, 255, 250))
    draw.text((80, height // 2 - 20), game.get("subtitle", "").upper(), fill=theme["accent"])

    draw.text((80, height // 2 + 40), f"RELEASE: {game.get('release_date', 'CLASSIFIED')} | DEVELOPER: {game.get('developer', 'Infinity Ward')}", fill=(180, 190, 180))
    draw.text((80, height // 2 + 70), f"STORAGE: {game.get('storage_gb', 80)} GB | PLATFORM: {game.get('install_platform', 'PC')}", fill=(140, 150, 140))

    output_path.parent.mkdir(parents=True, exist_ok=True)
    im.save(output_path, "JPEG", quality=85)


def fetch_or_create_artwork(game: Dict[str, Any]):
    """Ensure cover and banner exist for game, downloading from Steam or generating locally."""
    game_id = game["id"]
    cover_path = COVERS_DIR / f"{game_id}.jpg"
    banner_path = BANNERS_DIR / f"{game_id}.jpg"

    # 1. Try Steam CDN download if not already cached and steam_appid is valid
    steam_id = game.get("steam_appid", 0)
    if not cover_path.exists() and steam_id > 0:
        steam_urls = [
            f"https://shared.fastly.steamstatic.com/store_item_assets/steam/apps/{steam_id}/library_600x900_2x.jpg",
            f"https://cdn.cloudflare.steamstatic.com/steam/apps/{steam_id}/header.jpg"
        ]
        for url in steam_urls:
            try:
                res = requests.get(url, timeout=3)
                if res.status_code == 200 and len(res.content) > 1000:
                    with open(cover_path, "wb") as f:
                        f.write(res.content)
                    break
            except Exception:
                pass

    # 2. If cover still doesn't exist, procedurally generate it
    if not cover_path.exists():
        generate_tactical_cover(game, cover_path)

    # 3. Generate banner if not present
    if not banner_path.exists():
        generate_tactical_banner(game, banner_path)

    return {
        "cover": f"/assets/covers/{game_id}.jpg",
        "banner": f"/assets/banners/{game_id}.jpg"
    }


def generate_all_artwork():
    """Batch generate / verify artwork for all games in the franchise database."""
    from launcher.database import GAMES_DATABASE
    for game in GAMES_DATABASE.values():
        fetch_or_create_artwork(game)
