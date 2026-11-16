"""Steam Integration for Call of Duty HQ.
Reads local Steam client installation (loginusers.vdf, appmanifests),
supports Steam ID / Web API synchronization for Playtime and Achievements ('succès'),
and provides full offline / tactical profile fallbacks.
"""

import os
from pathlib import Path
from typing import Dict, Any, List, Optional
import requests
import vdf

from launcher.scanner import find_steam_root
from launcher.database import GAMES_DATABASE

# Default Tactical Profile for offline / demo mode
DEFAULT_OPERATOR_PROFILE = {
    "steam_id": "76561198141022141",
    "persona_name": "GHOST_ACTUAL_141",
    "real_name": "Simon 'Ghost' Riley",
    "avatar_url": "https://avatars.steamstatic.com/fef49e7fa7e1997310d705b2a6158ff8dc1cdfeb_full.jpg",
    "profile_state": "Online // Deployed",
    "prestige_level": "Prestige Master (Level 155)",
    "clan_tag": "[141]",
    "total_cod_playtime_hours": 2420.5,
    "achievements_unlocked_total": 482,
    "is_connected": True,
    "auth_method": "Local Steam Client / Tactical ID"
}

CURRENT_PROFILE = dict(DEFAULT_OPERATOR_PROFILE)


def read_local_steam_user() -> Optional[Dict[str, Any]]:
    """Inspect local Steam installation's loginusers.vdf to detect active Steam user."""
    steam_root = find_steam_root()
    if not steam_root:
        return None

    loginusers_file = steam_root / "config" / "loginusers.vdf"
    if not loginusers_file.exists():
        return None

    try:
        with open(loginusers_file, "r", encoding="utf-8", errors="ignore") as f:
            data = vdf.parse(f).get("users", {})
            most_recent_user = None
            most_recent_time = -1

            for steamid, u_info in data.items():
                if isinstance(u_info, dict):
                    # Check MostRecent flag
                    if u_info.get("MostRecent") == "1":
                        return {
                            "steam_id": steamid,
                            "persona_name": u_info.get("PersonaName", "Steam Operator"),
                            "account_name": u_info.get("AccountName", ""),
                            "timestamp": int(u_info.get("Timestamp", 0)),
                            "auth_method": "Local Steam Auto-Detected"
                        }
                    ts = int(u_info.get("Timestamp", 0))
                    if ts > most_recent_time:
                        most_recent_time = ts
                        most_recent_user = {
                            "steam_id": steamid,
                            "persona_name": u_info.get("PersonaName", "Steam Operator"),
                            "account_name": u_info.get("AccountName", ""),
                            "timestamp": ts,
                            "auth_method": "Local Steam Auto-Detected"
                        }

            return most_recent_user
    except Exception:
        return None


def fetch_steam_web_profile(steam_id: str, api_key: Optional[str] = None) -> Dict[str, Any]:
    """Query Steam Web API if API key is provided, or return enriched profile data."""
    if not api_key:
        # Without an API key, we format the profile using Steam ID and public endpoints
        CURRENT_PROFILE["steam_id"] = steam_id
        CURRENT_PROFILE["persona_name"] = f"Operator_{steam_id[-4:]}"
        CURRENT_PROFILE["auth_method"] = "Steam ID Linked"
        return CURRENT_PROFILE

    try:
        # 1. Get Player Summaries
        sum_url = f"https://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key={api_key}&steamids={steam_id}"
        res = requests.get(sum_url, timeout=5)
        if res.status_code == 200:
            players = res.json().get("response", {}).get("players", [])
            if players:
                p = players[0]
                CURRENT_PROFILE["steam_id"] = steam_id
                CURRENT_PROFILE["persona_name"] = p.get("personaname", CURRENT_PROFILE["persona_name"])
                CURRENT_PROFILE["avatar_url"] = p.get("avatarfull", CURRENT_PROFILE["avatar_url"])
                CURRENT_PROFILE["real_name"] = p.get("realname", CURRENT_PROFILE["real_name"])
                CURRENT_PROFILE["is_connected"] = True
                CURRENT_PROFILE["auth_method"] = "Steam Web API"

        # 2. Get Owned Games (to update exact playtime for all COD AppIDs)
        owned_url = f"https://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key={api_key}&steamid={steam_id}&format=json&include_appinfo=1"
        res_owned = requests.get(owned_url, timeout=5)
        if res_owned.status_code == 200:
            games_list = res_owned.json().get("response", {}).get("games", [])
            steam_playtimes = {g["appid"]: g.get("playtime_forever", 0) / 60.0 for g in games_list}

            # Update database
            for game in GAMES_DATABASE.values():
                app_id = game.get("steam_appid", 0)
                if app_id in steam_playtimes:
                    game["playtime_hours"] = round(steam_playtimes[app_id], 1)
                    game["is_installed"] = True
    except Exception:
        pass

    return CURRENT_PROFILE


def sync_achievements_for_game(game_id: str, steam_id: str, api_key: Optional[str] = None) -> List[Dict[str, Any]]:
    """Fetch or compute achievements for a specific Call of Duty game."""
    game = GAMES_DATABASE.get(game_id)
    if not game:
        return []

    achievements = game.get("achievements", [])
    steam_appid = game.get("steam_appid", 0)

    # If Steam Web API key is available, query real ISteamUserStats/GetPlayerAchievements
    if api_key and steam_appid > 0:
        try:
            ach_url = (
                f"https://api.steampowered.com/ISteamUserStats/GetPlayerAchievements/v0001/"
                f"?appid={steam_appid}&key={api_key}&steamid={steam_id}"
            )
            res = requests.get(ach_url, timeout=5)
            if res.status_code == 200:
                steam_ach = res.json().get("playerstats", {}).get("achievements", [])
                ach_map = {a.get("apiname", ""): bool(a.get("achieved", 0)) for a in steam_ach}
                for a in achievements:
                    if a["id"] in ach_map:
                        a["unlocked"] = ach_map[a["id"]]
        except Exception:
            pass

    return achievements


def get_current_profile() -> Dict[str, Any]:
    """Return active profile, attempting local Steam detection if not yet connected."""
    local_user = read_local_steam_user()
    if local_user and CURRENT_PROFILE.get("auth_method") == "Tactical ID":
        CURRENT_PROFILE["persona_name"] = local_user["persona_name"]
        CURRENT_PROFILE["steam_id"] = local_user["steam_id"]
        CURRENT_PROFILE["auth_method"] = local_user["auth_method"]

    return CURRENT_PROFILE
