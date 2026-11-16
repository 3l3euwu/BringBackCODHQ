"""Call of Duty HQ - Franchise Games Database.
Comprehensive catalog of every mainline Call of Duty title across franchise history.
Includes Steam AppIDs, Battle.net IDs, default executables, install paths,
modes, technical specs, and authentic achievements.
"""

from typing import Dict, Any, List

GAMES_DATABASE: Dict[str, Dict[str, Any]] = {
    "cod-bo6": {
        "id": "cod-bo6",
        "title": "Call of Duty: Black Ops 6",
        "subtitle": "The Truth Lies // Gulf War Era",
        "release_year": 2024,
        "release_date": "October 25, 2024",
        "series": "Black Ops",
        "developer": "Treyarch / Raven Software",
        "publisher": "Activision",
        "engine": "IW 9.0 (Unified COD Engine)",
        "steam_appid": 2933620,
        "battlenet_id": "AUUK",
        "xbox_store_id": "9PF4S13G80Z3",
        "default_exes": ["cod.exe", "bootstrapper.exe"],
        "default_dirs": [
            "Call of Duty",
            "Call of Duty HQ",
            "Call of Duty - Black Ops 6",
            "Call of Duty Black Ops 6"
        ],
        "modes": ["Campaign", "Multiplayer", "Round-Based Zombies", "Warzone Integration"],
        "storage_gb": 145,
        "is_installed": True,
        "installed_path": "C:\\Program Files (x86)\\Steam\\steamapps\\common\\Call of Duty HQ\\cod.exe",
        "install_platform": "Steam",
        "playtime_hours": 128.5,
        "last_played": "Today, 14:22",
        "is_favorite": True,
        "launch_args": "-d3d11 -novid",
        "synopsis": (
            "Set in the early 1990s following the end of the Cold War and the collapse of the Soviet Union, "
            "rogue operative Troy Marshall and Frank Woods uncover a shadow conspiracy within the highest ranks of the CIA. "
            "Featuring mind-bending campaign storytelling, omnimovement tactical combat, and the return of classic Round-Based Zombies."
        ),
        "specs": {
            "min_os": "Windows 10 64-bit (latest update)",
            "min_cpu": "AMD Ryzen 5 1400 / Intel Core i5-6600",
            "min_ram": "8 GB RAM",
            "min_gpu": "AMD Radeon RX 470 / NVIDIA GeForce GTX 960",
            "rec_os": "Windows 11 64-bit",
            "rec_cpu": "AMD Ryzen 5 1600X / Intel Core i7-6700K",
            "rec_ram": "16 GB RAM",
            "rec_gpu": "AMD Radeon RX 6600 XT / NVIDIA GeForce RTX 3060"
        },
        "achievements": [
            {"id": "bo6_01", "name": "The Truth Lies", "desc": "Complete the Campaign on any difficulty.", "unlocked": True, "icon": "shield"},
            {"id": "bo6_02", "name": "Omni-Dominance", "desc": "Perform 50 sprint-slide-dive kills in Multiplayer.", "unlocked": True, "icon": "target"},
            {"id": "bo6_03", "name": "Terminus Awakening", "desc": "Solve the main easter egg protocol in Terminus Island.", "unlocked": True, "icon": "skull"},
            {"id": "bo6_04", "name": "Liberty Falls Survivor", "desc": "Reach Round 30 without using armor plates in Liberty Falls.", "unlocked": False, "icon": "hazard"},
            {"id": "bo6_05", "name": "Black Ops Operative", "desc": "Complete the Campaign on Veteran difficulty.", "unlocked": False, "icon": "star"},
            {"id": "bo6_06", "name": "Prestige Master", "desc": "Enter Classic Prestige 1 in Multiplayer.", "unlocked": True, "icon": "medal"}
        ]
    },
    "cod-mw3-2023": {
        "id": "cod-mw3-2023",
        "title": "Call of Duty: Modern Warfare III",
        "subtitle": "The Ultimate Threat Returns // Makarov",
        "release_year": 2023,
        "release_date": "November 10, 2023",
        "series": "Modern Warfare",
        "developer": "Sledgehammer Games / Infinity Ward",
        "publisher": "Activision",
        "engine": "IW 9.0",
        "steam_appid": 2519060,
        "battlenet_id": "AUUK",
        "default_exes": ["cod.exe"],
        "default_dirs": ["Call of Duty", "Call of Duty Modern Warfare III"],
        "modes": ["Campaign", "Multiplayer", "Open-World Zombies (MWZ)", "Warzone Integration"],
        "storage_gb": 130,
        "is_installed": True,
        "installed_path": "C:\\Program Files (x86)\\Steam\\steamapps\\common\\Call of Duty HQ\\cod.exe",
        "install_platform": "Steam",
        "playtime_hours": 214.2,
        "last_played": "Yesterday",
        "is_favorite": True,
        "launch_args": "",
        "synopsis": (
            "Captain Price and Task Force 141 face the ultimate threat: ultranationalist Vladimir Makarov, "
            "extending his grasp across the world and causing Task Force 141 to fight like never before. "
            "Includes all 16 modernized launch maps from MW2 (2009)."
        ),
        "specs": {
            "min_os": "Windows 10 64-bit",
            "min_cpu": "Intel Core i5-6600 / AMD Ryzen 5 1400",
            "min_ram": "8 GB",
            "min_gpu": "NVIDIA GeForce GTX 960 / GTX 1650 / AMD RX 470",
            "rec_os": "Windows 11 64-bit",
            "rec_cpu": "Intel Core i7-6700K / AMD Ryzen 5 1600X",
            "rec_ram": "16 GB",
            "rec_gpu": "NVIDIA GeForce RTX 3060 / AMD RX 6600 XT"
        },
        "achievements": [
            {"id": "mw3_01", "name": "Never Back Down", "desc": "Infiltrate Makarov's stronghold in Operation 627.", "unlocked": True, "icon": "shield"},
            {"id": "mw3_02", "name": "Highjacked", "desc": "Intercept the chemical convoy across Urzikstan.", "unlocked": True, "icon": "truck"},
            {"id": "mw3_03", "name": "MWZ Exfil Master", "desc": "Successfully exfil 50 times from Dark Aether in Modern Warfare Zombies.", "unlocked": True, "icon": "skull"},
            {"id": "mw3_04", "name": "141 Brotherhood", "desc": "Complete all Campaign Open Combat missions on Veteran.", "unlocked": False, "icon": "star"}
        ]
    },
    "cod-mw2-2022": {
        "id": "cod-mw2-2022",
        "title": "Call of Duty: Modern Warfare II",
        "subtitle": "Task Force 141 Global Recon",
        "release_year": 2022,
        "release_date": "October 28, 2022",
        "series": "Modern Warfare",
        "developer": "Infinity Ward",
        "publisher": "Activision",
        "engine": "IW 9.0",
        "steam_appid": 1938090,
        "battlenet_id": "AUUK",
        "default_exes": ["cod.exe"],
        "default_dirs": ["Call of Duty", "Call of Duty Modern Warfare II"],
        "modes": ["Campaign", "Multiplayer", "Special Ops Raids", "DMZ", "Warzone 2.0"],
        "storage_gb": 115,
        "is_installed": False,
        "installed_path": "",
        "install_platform": "Steam",
        "playtime_hours": 182.0,
        "last_played": "August 14, 2024",
        "is_favorite": False,
        "launch_args": "",
        "synopsis": (
            "Drop into global conflict with the return of Task Force 141: Captain John Price, Kyle 'Gaz' Garrick, "
            "Simon 'Ghost' Riley, and John 'Soap' MacTavish. Engage in high-stakes operations across Mexico, Europe, and the Middle East."
        ),
        "specs": {
            "min_os": "Windows 10 64-bit",
            "min_cpu": "Intel Core i3-6100 / AMD Ryzen 3 1200",
            "min_ram": "8 GB",
            "min_gpu": "NVIDIA GeForce GTX 960 / AMD Radeon RX 470",
            "rec_os": "Windows 10/11 64-bit",
            "rec_cpu": "Intel Core i5-6600K / AMD Ryzen 5 1400",
            "rec_ram": "12 GB",
            "rec_gpu": "NVIDIA GeForce GTX 1060 / AMD Radeon RX 580"
        },
        "achievements": [
            {"id": "mw2_01", "name": "Ghost of Las Almas", "desc": "Survive the ambush in Alone without firing a weapon.", "unlocked": True, "icon": "skull"},
            {"id": "mw2_02", "name": "Time is of the Essence", "desc": "Complete the Clean House raid in under 4 minutes.", "unlocked": True, "icon": "target"},
            {"id": "mw2_03", "name": "Veteran Operator", "desc": "Finish Campaign on Veteran.", "unlocked": False, "icon": "medal"}
        ]
    },
    "cod-warzone": {
        "id": "cod-warzone",
        "title": "Call of Duty: Warzone",
        "subtitle": "Free-to-Play Battle Royale & Resurgence",
        "release_year": 2020,
        "release_date": "March 10, 2020",
        "series": "Warzone",
        "developer": "Raven Software / Infinity Ward",
        "publisher": "Activision",
        "engine": "IW 8.0 / IW 9.0",
        "steam_appid": 1938090,
        "battlenet_id": "AUUK",
        "default_exes": ["cod.exe", "ModernWarfare.exe"],
        "default_dirs": ["Call of Duty", "Call of Duty Modern Warfare"],
        "modes": ["Battle Royale", "Resurgence", "Plunder", "Bootcamp", "Ranked Play"],
        "storage_gb": 85,
        "is_installed": True,
        "installed_path": "C:\\Program Files (x86)\\Steam\\steamapps\\common\\Call of Duty HQ\\cod.exe",
        "install_platform": "Steam",
        "playtime_hours": 420.7,
        "last_played": "3 days ago",
        "is_favorite": True,
        "launch_args": "-warzone",
        "synopsis": (
            "Drop in, armor up, loot for rewards, and battle your way to the top in the massive free-to-play "
            "combat arena featuring Verdansk, Urzikstan, Rebirth Island, and Fortune's Keep."
        ),
        "specs": {
            "min_os": "Windows 10 64-bit",
            "min_cpu": "Intel Core i3-6100 / AMD Ryzen 3 1200",
            "min_ram": "8 GB",
            "min_gpu": "NVIDIA GeForce GTX 960 / AMD Radeon RX 470",
            "rec_os": "Windows 11 64-bit",
            "rec_cpu": "Intel Core i7-8700K / AMD Ryzen 7 2700X",
            "rec_ram": "16 GB",
            "rec_gpu": "NVIDIA GeForce RTX 3070 / AMD Radeon RX 6800 XT"
        },
        "achievements": [
            {"id": "wz_01", "name": "Gulag Champion", "desc": "Win 100 1v1 fights in the Gulag.", "unlocked": True, "icon": "skull"},
            {"id": "wz_02", "name": "Victory Royale", "desc": "Claim 1st place in Battle Royale Squads.", "unlocked": True, "icon": "trophy"},
            {"id": "wz_03", "name": "Resurgence King", "desc": "Achieve 20 squad wipes in Rebirth Island.", "unlocked": True, "icon": "target"}
        ]
    },
    "cod-vanguard": {
        "id": "cod-vanguard",
        "title": "Call of Duty: Vanguard",
        "subtitle": "Rise on Every Front // WWII Special Forces",
        "release_year": 2021,
        "release_date": "November 5, 2021",
        "series": "World War II",
        "developer": "Sledgehammer Games",
        "publisher": "Activision",
        "engine": "IW 8.0",
        "steam_appid": 1985820,
        "battlenet_id": "FORE",
        "default_exes": ["Vanguard.exe"],
        "default_dirs": ["Call of Duty Vanguard"],
        "modes": ["Campaign", "Multiplayer", "Der Anfang Zombies", "Champion Hill"],
        "storage_gb": 68,
        "is_installed": False,
        "installed_path": "",
        "install_platform": "Steam",
        "playtime_hours": 34.0,
        "last_played": "March 2023",
        "is_favorite": False,
        "launch_args": "",
        "synopsis": (
            "Witness the origins of Special Forces in World War II. Fight as Task Force One across the Eastern and Western "
            "Fronts of Europe, the Pacific, and North Africa to destroy Project Phoenix."
        ),
        "specs": {
            "min_os": "Windows 10 64-bit",
            "min_cpu": "Intel Core i3-4340 / AMD FX-6300",
            "min_ram": "8 GB",
            "min_gpu": "NVIDIA GeForce GTX 960 / AMD Radeon RX 470",
            "rec_os": "Windows 10 64-bit",
            "rec_cpu": "Intel Core i5-2500K / AMD Ryzen 5 1600X",
            "rec_ram": "12 GB",
            "rec_gpu": "NVIDIA GeForce GTX 1060 / AMD Radeon RX 580"
        },
        "achievements": [
            {"id": "van_01", "name": "Phoenix Down", "desc": "Uncover the secrets of Project Phoenix.", "unlocked": True, "icon": "shield"},
            {"id": "van_02", "name": "Aces High", "desc": "Shoot down 15 Stuka dive-bombers over Midway.", "unlocked": False, "icon": "target"}
        ]
    },
    "cod-cold-war": {
        "id": "cod-cold-war",
        "title": "Call of Duty: Black Ops Cold War",
        "subtitle": "Know Your History // Perseus Protocol",
        "release_year": 2020,
        "release_date": "November 13, 2020",
        "series": "Black Ops",
        "developer": "Treyarch / Raven Software",
        "publisher": "Activision",
        "engine": "Treyarch Black Ops Engine",
        "steam_appid": 1985810,
        "battlenet_id": "ZEUS",
        "default_exes": ["BlackOpsColdWar.exe"],
        "default_dirs": ["Call of Duty Black Ops Cold War"],
        "modes": ["Campaign", "Multiplayer", "Dark Aether Zombies", "Outbreak", "Dead Ops Arcade 3"],
        "storage_gb": 125,
        "is_installed": True,
        "installed_path": "C:\\Program Files (x86)\\Steam\\steamapps\\common\\Call of Duty Black Ops Cold War\\BlackOpsColdWar.exe",
        "install_platform": "Steam",
        "playtime_hours": 164.8,
        "last_played": "October 2024",
        "is_favorite": True,
        "launch_args": "",
        "synopsis": (
            "Drop into the geopolitical depths of the Cold War in the early 1980s. Come face-to-face with historical figures "
            "as you track down a Soviet spy named Perseus alongside Frank Woods, Alex Mason, and Russell Adler."
        ),
        "specs": {
            "min_os": "Windows 10 64-bit",
            "min_cpu": "Intel Core i3-4340 / AMD FX-6300",
            "min_ram": "8 GB",
            "min_gpu": "NVIDIA GeForce GTX 670 / AMD Radeon HD 7950",
            "rec_os": "Windows 10 64-bit",
            "rec_cpu": "Intel Core i5-2500K / AMD Ryzen R5 1600X",
            "rec_ram": "12 GB",
            "rec_gpu": "NVIDIA GeForce GTX 970 / AMD Radeon R9 390"
        },
        "achievements": [
            {"id": "cw_01", "name": "Bell's Choice", "desc": "Make the final decision at Duga radar facility.", "unlocked": True, "icon": "shield"},
            {"id": "cw_02", "name": "Die Maschine Seal", "desc": "Close the dimensional rift in Die Maschine.", "unlocked": True, "icon": "skull"},
            {"id": "cw_03", "name": "Red Door Truth", "desc": "Relive the interrogation without disobeying Adler.", "unlocked": True, "icon": "star"}
        ]
    },
    "cod-mw-2019": {
        "id": "cod-mw-2019",
        "title": "Call of Duty: Modern Warfare (2019)",
        "subtitle": "Going Dark // The Gritty Reboot",
        "release_year": 2019,
        "release_date": "October 25, 2019",
        "series": "Modern Warfare",
        "developer": "Infinity Ward",
        "publisher": "Activision",
        "engine": "IW 8.0 (Rebuilt Engine)",
        "steam_appid": 2000950,
        "battlenet_id": "ODIN",
        "default_exes": ["ModernWarfare.exe"],
        "default_dirs": ["Call of Duty Modern Warfare"],
        "modes": ["Campaign", "Multiplayer", "Special Ops", "Ground War", "Gunfight"],
        "storage_gb": 175,
        "is_installed": True,
        "installed_path": "C:\\Program Files (x86)\\Battle.net\\Call of Duty Modern Warfare\\ModernWarfare.exe",
        "install_platform": "Battle.net",
        "playtime_hours": 312.4,
        "last_played": "September 2024",
        "is_favorite": True,
        "launch_args": "",
        "synopsis": (
            "The iconic series reboot that redefined tactical first-person shooters. Captain John Price works with the CIA "
            "and Urzikstan Liberation Force to retrieve stolen chemical weapons in visceral night-vision raids such as 'Clean House'."
        ),
        "specs": {
            "min_os": "Windows 10 64-bit",
            "min_cpu": "Intel Core i3-4340 / AMD FX-6300",
            "min_ram": "8 GB",
            "min_gpu": "NVIDIA GeForce GTX 670 / AMD Radeon HD 7950",
            "rec_os": "Windows 10 64-bit",
            "rec_cpu": "Intel Core i5-2500K / AMD Ryzen R5 1600X",
            "rec_ram": "12 GB",
            "rec_gpu": "NVIDIA GeForce GTX 970 / AMD Radeon R9 390"
        },
        "achievements": [
            {"id": "mw19_01", "name": "Clean House", "desc": "Complete 'Clean House' without taking damage or killing civilians.", "unlocked": True, "icon": "skull"},
            {"id": "mw19_02", "name": "Going Dark", "desc": "Turn off power in 4 buildings during Going Dark.", "unlocked": True, "icon": "target"},
            {"id": "mw19_03", "name": "Tea Time", "desc": "Complete the Campaign on Veteran.", "unlocked": True, "icon": "medal"}
        ]
    },
    "cod-mw2-cr": {
        "id": "cod-mw2-cr",
        "title": "Call of Duty: Modern Warfare 2 Campaign Remastered",
        "subtitle": "Relive the Iconic 2009 Campaign in Full 4K HDR",
        "release_year": 2020,
        "release_date": "April 30, 2020",
        "series": "Modern Warfare",
        "developer": "Beenox / Infinity Ward",
        "publisher": "Activision",
        "engine": "IW 7.0 Remastered",
        "steam_appid": 2000950,
        "battlenet_id": "LAZR",
        "default_exes": ["MW2CR.exe"],
        "default_dirs": ["Call of Duty Modern Warfare 2 Campaign Remastered"],
        "modes": ["Campaign"],
        "storage_gb": 45,
        "is_installed": False,
        "installed_path": "",
        "install_platform": "Battle.net",
        "playtime_hours": 18.5,
        "last_played": "May 2021",
        "is_favorite": False,
        "launch_args": "",
        "synopsis": (
            "Experience the legendary single-player campaign from 2009's Modern Warfare 2, completely remastered with "
            "improved textures, animations, physically based rendering, and high-dynamic range lighting."
        ),
        "specs": {
            "min_os": "Windows 7/8/10 64-bit",
            "min_cpu": "Intel Core i3-4340 / AMD FX-6300",
            "min_ram": "8 GB",
            "min_gpu": "NVIDIA GeForce GTX 670 / AMD Radeon HD 7950",
            "rec_os": "Windows 10 64-bit",
            "rec_cpu": "Intel Core i5-2500K / AMD Ryzen R5 1600X",
            "rec_ram": "12 GB",
            "rec_gpu": "NVIDIA GeForce GTX 970 / AMD Radeon R9 390"
        },
        "achievements": [
            {"id": "mw2cr_01", "name": "The Price of War", "desc": "Complete the single player campaign on Hardened or Veteran.", "unlocked": True, "icon": "medal"},
            {"id": "mw2cr_02", "name": "Immortal", "desc": "Complete every mission without dying or reloading a checkpoint.", "unlocked": False, "icon": "skull"}
        ]
    },
    "cod-bo4": {
        "id": "cod-bo4",
        "title": "Call of Duty: Black Ops 4",
        "subtitle": "Forget What You Know // Blackout Battle Royale",
        "release_year": 2018,
        "release_date": "October 12, 2018",
        "series": "Black Ops",
        "developer": "Treyarch",
        "publisher": "Activision",
        "engine": "Black Ops Engine",
        "steam_appid": 0,
        "battlenet_id": "VIPR",
        "default_exes": ["BlackOps4.exe"],
        "default_dirs": ["Call of Duty Black Ops 4"],
        "modes": ["Blackout Battle Royale", "Multiplayer", "Aether & Chaos Zombies", "Specialist HQ"],
        "storage_gb": 110,
        "is_installed": False,
        "installed_path": "",
        "install_platform": "Battle.net",
        "playtime_hours": 95.0,
        "last_played": "January 2021",
        "is_favorite": False,
        "launch_args": "",
        "synopsis": (
            "Grounded, fluid tactical multiplayer combat, the biggest Zombies offering ever at launch with four distinct adventures, "
            "and Blackout, where the Black Ops universe comes to life in a massive battle royale experience."
        ),
        "specs": {
            "min_os": "Windows 7 64-bit",
            "min_cpu": "Intel Core i3-4340 / AMD FX-6300",
            "min_ram": "8 GB",
            "min_gpu": "NVIDIA GeForce GTX 660 / AMD Radeon HD 7950",
            "rec_os": "Windows 10 64-bit",
            "rec_cpu": "Intel Core i5-2500K / Ryzen R5 1600X",
            "rec_ram": "12 GB",
            "rec_gpu": "NVIDIA GeForce GTX 970 / AMD Radeon R9 390"
        },
        "achievements": [
            {"id": "bo4_01", "name": "Blackout Victor", "desc": "Win a game of Blackout.", "unlocked": True, "icon": "trophy"},
            {"id": "bo4_02", "name": "Valkyrie Ally", "desc": "Solve the Voyage of Despair mystery.", "unlocked": False, "icon": "skull"}
        ]
    },
    "cod-wwii": {
        "id": "cod-wwii",
        "title": "Call of Duty: WWII",
        "subtitle": "Boots on the Ground // Normandy to the Rhine",
        "release_year": 2017,
        "release_date": "November 3, 2017",
        "series": "World War II",
        "developer": "Sledgehammer Games",
        "publisher": "Activision",
        "engine": "Sledgehammer Engine",
        "steam_appid": 596350,
        "battlenet_id": "",
        "default_exes": ["s2_sp64_ship.exe", "s2_mp64_ship.exe"],
        "default_dirs": ["Call of Duty WWII"],
        "modes": ["Campaign", "Multiplayer", "Nazi Zombies", "War Mode"],
        "storage_gb": 90,
        "is_installed": False,
        "installed_path": "",
        "install_platform": "Steam",
        "playtime_hours": 48.0,
        "last_played": "2020",
        "is_favorite": False,
        "launch_args": "",
        "synopsis": (
            "Return to the roots of the franchise. Experience the dramatic story of the US 1st Infantry Division "
            "from the beaches of Normandy through the liberation of Paris and the Battle of the Bulge."
        ),
        "specs": {
            "min_os": "Windows 7 64-bit",
            "min_cpu": "Intel Core i3-3225 / AMD Ryzen 5 1400",
            "min_ram": "8 GB",
            "min_gpu": "NVIDIA GeForce GTX 660 / AMD Radeon HD 7850",
            "rec_os": "Windows 10 64-bit",
            "rec_cpu": "Intel Core i5-2400 / AMD Ryzen R5 1600X",
            "rec_ram": "12 GB",
            "rec_gpu": "NVIDIA GeForce GTX 970 / AMD Radeon R9 390"
        },
        "achievements": [
            {"id": "ww2_01", "name": "To the End", "desc": "Complete the campaign.", "unlocked": True, "icon": "shield"},
            {"id": "ww2_02", "name": "Dark Reunion", "desc": "Save Klaus in The Final Reich.", "unlocked": False, "icon": "skull"}
        ]
    },
    "cod-iw": {
        "id": "cod-iw",
        "title": "Call of Duty: Infinite Warfare",
        "subtitle": "Fight Across the Solar System // Retribution",
        "release_year": 2016,
        "release_date": "November 4, 2016",
        "series": "Advanced & Futuristic",
        "developer": "Infinity Ward",
        "publisher": "Activision",
        "engine": "IW 7.0",
        "steam_appid": 292730,
        "battlenet_id": "",
        "default_exes": ["InfiniteWarfare.exe"],
        "default_dirs": ["Call of Duty - Infinite Warfare", "Call of Duty Infinite Warfare"],
        "modes": ["Campaign", "Multiplayer", "Zombies in Spaceland", "Jackal VR"],
        "storage_gb": 80,
        "is_installed": False,
        "installed_path": "",
        "install_platform": "Steam",
        "playtime_hours": 31.0,
        "last_played": "2019",
        "is_favorite": False,
        "launch_args": "",
        "synopsis": (
            "Take command of the UNSA warship Retribution as Captain Nick Reyes. Lead coalition forces against the ruthless "
            "Settlement Defense Front led by Salen Kotch across planetary battlegrounds and deep space fighter dogfights."
        ),
        "specs": {
            "min_os": "Windows 7 64-bit",
            "min_cpu": "Intel Core i3-3225 @ 3.30GHz",
            "min_ram": "8 GB",
            "min_gpu": "NVIDIA GeForce GTX 660 / AMD Radeon HD 7850",
            "rec_os": "Windows 10 64-bit",
            "rec_cpu": "Intel Core i5-4460 / AMD FX-8350",
            "rec_ram": "16 GB",
            "rec_gpu": "NVIDIA GeForce GTX 970 / AMD Radeon R9 390"
        },
        "achievements": [
            {"id": "iw_01", "name": "Peace to the Fallen", "desc": "Complete the Campaign.", "unlocked": True, "icon": "shield"},
            {"id": "iw_02", "name": "Sooo 80s", "desc": "Find the MW1 easter egg in Spaceland.", "unlocked": False, "icon": "star"}
        ]
    },
    "cod-mwr": {
        "id": "cod-mwr",
        "title": "Call of Duty: Modern Warfare Remastered",
        "subtitle": "The Definitive Remaster of the 2007 Classic",
        "release_year": 2016,
        "release_date": "November 4, 2016",
        "series": "Modern Warfare",
        "developer": "Raven Software / Infinity Ward",
        "publisher": "Activision",
        "engine": "IW 7.0 (MWR)",
        "steam_appid": 476600,
        "battlenet_id": "",
        "default_exes": ["h1_sp64_ship.exe", "h1_mp64_ship.exe"],
        "default_dirs": ["Call of Duty Modern Warfare Remastered"],
        "modes": ["Campaign", "Multiplayer"],
        "storage_gb": 55,
        "is_installed": True,
        "installed_path": "C:\\Program Files (x86)\\Steam\\steamapps\\common\\Call of Duty Modern Warfare Remastered\\h1_sp64_ship.exe",
        "install_platform": "Steam",
        "playtime_hours": 76.2,
        "last_played": "July 2024",
        "is_favorite": True,
        "launch_args": "",
        "synopsis": (
            "One of the most critically acclaimed games in history, remastered in true high-definition with "
            "physically based rendering, updated animations, remastered audio, and full multiplayer support."
        ),
        "specs": {
            "min_os": "Windows 7 64-bit",
            "min_cpu": "Intel Core i3-3225 @ 3.30GHz",
            "min_ram": "8 GB",
            "min_gpu": "NVIDIA GeForce GTX 660 / AMD Radeon HD 7850",
            "rec_os": "Windows 10 64-bit",
            "rec_cpu": "Intel Core i5-4590",
            "rec_ram": "16 GB",
            "rec_gpu": "NVIDIA GeForce GTX 970"
        },
        "achievements": [
            {"id": "mwr_01", "name": "Mile High Club", "desc": "Sky dive to safety on Veteran difficulty.", "unlocked": True, "icon": "skull"},
            {"id": "mwr_02", "name": "Deep and Hard", "desc": "Complete the Campaign on Hardened or Veteran.", "unlocked": True, "icon": "medal"},
            {"id": "mwr_03", "name": "Eyes and Ears", "desc": "Find 30 enemy intel items.", "unlocked": True, "icon": "target"}
        ]
    },
    "cod-bo3": {
        "id": "cod-bo3",
        "title": "Call of Duty: Black Ops III",
        "subtitle": "How Far Do We Go? // Zombies Chronicles",
        "release_year": 2015,
        "release_date": "November 6, 2015",
        "series": "Black Ops",
        "developer": "Treyarch",
        "publisher": "Activision",
        "engine": "Black Ops Engine",
        "steam_appid": 311210,
        "battlenet_id": "",
        "default_exes": ["BlackOps3.exe"],
        "default_dirs": ["Call of Duty Black Ops III", "Call of Duty Black Ops 3"],
        "modes": ["4-Player Co-op Campaign", "Multiplayer", "Shadows of Evil Zombies", "Zombies Chronicles", "Nightmares"],
        "storage_gb": 120,
        "is_installed": True,
        "installed_path": "C:\\Program Files (x86)\\Steam\\steamapps\\common\\Call of Duty Black Ops III\\BlackOps3.exe",
        "install_platform": "Steam",
        "playtime_hours": 389.0,
        "last_played": "Last week",
        "is_favorite": True,
        "launch_args": "",
        "synopsis": (
            "In 2065, cybernetic enhancements blur the line between humanity and warfare. Features steam workshop custom "
            "zombies maps, momentum-based chained movement, and the definitive Zombies Chronicles expansion."
        ),
        "specs": {
            "min_os": "Windows 7 64-bit",
            "min_cpu": "Intel Core i3-530 @ 2.93 GHz / AMD Phenom II X4 810",
            "min_ram": "6 GB",
            "min_gpu": "NVIDIA GeForce GTX 470 / AMD Radeon HD 6970",
            "rec_os": "Windows 10 64-bit",
            "rec_cpu": "Intel Core i5-4460",
            "rec_ram": "12 GB",
            "rec_gpu": "NVIDIA GeForce GTX 970"
        },
        "achievements": [
            {"id": "bo3_01", "name": "Apocalypse Averted", "desc": "In Shadows of Evil, defeat the Shadowman.", "unlocked": True, "icon": "skull"},
            {"id": "bo3_02", "name": "Der Eisendrache Master", "desc": "Upgrade all four ancient Wrath of the Ancients bows.", "unlocked": True, "icon": "target"},
            {"id": "bo3_03", "name": "Gorod Krovi Reclaimed", "desc": "Free Nikolai and defeat the dragon.", "unlocked": False, "icon": "star"},
            {"id": "bo3_04", "name": "For the Good of All", "desc": "In Revelations, complete the Cycle.", "unlocked": True, "icon": "medal"}
        ]
    },
    "cod-aw": {
        "id": "cod-aw",
        "title": "Call of Duty: Advanced Warfare",
        "subtitle": "Power Changes Everything // Exo-Suit Era",
        "release_year": 2014,
        "release_date": "November 4, 2014",
        "series": "Advanced & Futuristic",
        "developer": "Sledgehammer Games",
        "publisher": "Activision",
        "engine": "Sledgehammer Custom IW",
        "steam_appid": 209650,
        "battlenet_id": "",
        "default_exes": ["s1_sp64_ship.exe", "s1_mp64_ship.exe"],
        "default_dirs": ["Call of Duty Advanced Warfare"],
        "modes": ["Campaign", "Multiplayer", "Exo Zombies", "Exo Survival"],
        "storage_gb": 55,
        "is_installed": False,
        "installed_path": "",
        "install_platform": "Steam",
        "playtime_hours": 42.0,
        "last_played": "2018",
        "is_favorite": False,
        "launch_args": "",
        "synopsis": (
            "Envisioning the powerful battlegrounds of the future where private military corporations rule. "
            "Equip high-tech Exoskeletons that transform combat with boost jumping, grappling, and cloaking."
        ),
        "specs": {
            "min_os": "Windows 7 64-bit",
            "min_cpu": "Intel Core i3-530 @ 2.93 GHz / AMD Phenom II X4 810",
            "min_ram": "6 GB",
            "min_gpu": "NVIDIA GeForce GTS 450 / AMD Radeon HD 5870",
            "rec_os": "Windows 10 64-bit",
            "rec_cpu": "Intel Core i5-2500K @ 3.30GHz",
            "rec_ram": "8 GB",
            "rec_gpu": "NVIDIA GeForce GTX 760"
        },
        "achievements": [
            {"id": "aw_01", "name": "A New Era", "desc": "Complete the Campaign on any difficulty.", "unlocked": True, "icon": "shield"},
            {"id": "aw_02", "name": "Exo Survivor", "desc": "Successfully unlock Exo Zombies mode.", "unlocked": True, "icon": "skull"}
        ]
    },
    "cod-ghosts": {
        "id": "cod-ghosts",
        "title": "Call of Duty: Ghosts",
        "subtitle": "There are Those Who Refuse to Go Quietly // Extinction",
        "release_year": 2013,
        "release_date": "November 5, 2013",
        "series": "Modern Warfare",
        "developer": "Infinity Ward",
        "publisher": "Activision",
        "engine": "IW 6.0",
        "steam_appid": 209160,
        "battlenet_id": "",
        "default_exes": ["iw6sp64_ship.exe", "iw6mp64_ship.exe"],
        "default_dirs": ["Call of Duty Ghosts"],
        "modes": ["Campaign", "Multiplayer", "Extinction (Cryptids)", "Squads"],
        "storage_gb": 40,
        "is_installed": False,
        "installed_path": "",
        "install_platform": "Steam",
        "playtime_hours": 51.5,
        "last_played": "2017",
        "is_favorite": False,
        "launch_args": "",
        "synopsis": (
            "A devastating orbital kinetic strike devastates the United States. A decade later, an elite special operations "
            "unit known as the Ghosts fights back against the Federation of the Americas."
        ),
        "specs": {
            "min_os": "Windows 7 64-bit",
            "min_cpu": "Intel Core 2 Duo E8200 @ 2.66 GHZ",
            "min_ram": "6 GB",
            "min_gpu": "NVIDIA GeForce GTS 450 / ATI Radeon HD 5870",
            "rec_os": "Windows 10 64-bit",
            "rec_cpu": "Intel Core i5 – 680 @ 3.6GHz",
            "rec_ram": "8 GB",
            "rec_gpu": "NVIDIA GeForce GTX 760"
        },
        "achievements": [
            {"id": "gh_01", "name": "Ghost Stories", "desc": "Escape the ODIN space station.", "unlocked": True, "icon": "shield"},
            {"id": "gh_02", "name": "No Man's Land", "desc": "Survive the Federation crossing with Riley.", "unlocked": True, "icon": "target"},
            {"id": "gh_03", "name": "City Crasher", "desc": "Nuke the Cryptid hive in Extinction.", "unlocked": False, "icon": "skull"}
        ]
    },
    "cod-bo2": {
        "id": "cod-bo2",
        "title": "Call of Duty: Black Ops II",
        "subtitle": "2025 Cyber Warfare & Cold War Origins // Raul Menendez",
        "release_year": 2012,
        "release_date": "November 12, 2012",
        "series": "Black Ops",
        "developer": "Treyarch",
        "publisher": "Activision",
        "engine": "Black Ops II Engine",
        "steam_appid": 202970,
        "battlenet_id": "",
        "default_exes": ["t6sp.exe", "t6mp.exe", "t6zm.exe"],
        "default_dirs": ["Call of Duty Black Ops II", "Call of Duty Black Ops 2"],
        "modes": ["Branching Campaign", "Multiplayer (League Play)", "Tranzit / Mob of the Dead Zombies"],
        "storage_gb": 28,
        "is_installed": True,
        "installed_path": "C:\\Program Files (x86)\\Steam\\steamapps\\common\\Call of Duty Black Ops II\\t6sp.exe",
        "install_platform": "Steam",
        "playtime_hours": 245.0,
        "last_played": "September 2024",
        "is_favorite": True,
        "launch_args": "",
        "synopsis": (
            "A time-spanning narrative spanning the 1980s Cold War and 2025. Raul Menendez hijacks the US drone fleet. "
            "Pioneered branching campaign storylines, Pick 10 create-a-class, and legendary Zombies maps like Mob of the Dead and Origins."
        ),
        "specs": {
            "min_os": "Windows Vista SP2 / 7 / 10",
            "min_cpu": "Intel Core 2 Duo E8200 2.66 GHz / AMD Phenom X3 8750",
            "min_ram": "4 GB",
            "min_gpu": "NVIDIA GeForce 8800GT 512 MB / ATI Radeon HD 3870",
            "rec_os": "Windows 10 64-bit",
            "rec_cpu": "Intel Core i5-2500K",
            "rec_ram": "8 GB",
            "rec_gpu": "NVIDIA GeForce GTX 660"
        },
        "achievements": [
            {"id": "bo2_01", "name": "No Man Left Behind", "desc": "Rescue Frank Woods from the shipping container in Angola.", "unlocked": True, "icon": "shield"},
            {"id": "bo2_02", "name": "Tower of Babble", "desc": "In TranZit, obey Richtofen's voices.", "unlocked": True, "icon": "skull"},
            {"id": "bo2_03", "name": "Pop Goes the Weasel", "desc": "In Mob of the Dead, break the cycle.", "unlocked": True, "icon": "target"},
            {"id": "bo2_04", "name": "Little Lost Girl", "desc": "In Origins, release Samantha to Agartha.", "unlocked": True, "icon": "star"}
        ]
    },
    "cod-mw3-2011": {
        "id": "cod-mw3-2011",
        "title": "Call of Duty: Modern Warfare 3 (2011)",
        "subtitle": "World War III // The Epic Finale to the Original Trilogy",
        "release_year": 2011,
        "release_date": "November 8, 2011",
        "series": "Modern Warfare",
        "developer": "Infinity Ward / Sledgehammer Games",
        "publisher": "Activision",
        "engine": "MW3 Engine (IW 5.0)",
        "steam_appid": 115300,
        "battlenet_id": "",
        "default_exes": ["iw5sp.exe", "iw5mp.exe"],
        "default_dirs": ["Call of Duty Modern Warfare 3", "Modern Warfare 3"],
        "modes": ["Campaign", "Multiplayer", "Survival Mode", "Spec Ops Missions"],
        "storage_gb": 16,
        "is_installed": True,
        "installed_path": "C:\\Program Files (x86)\\Steam\\steamapps\\common\\Call of Duty Modern Warfare 3\\iw5sp.exe",
        "install_platform": "Steam",
        "playtime_hours": 112.0,
        "last_played": "2023",
        "is_favorite": True,
        "launch_args": "",
        "synopsis": (
            "The direct conclusion to Modern Warfare 2. Russian forces invade Manhattan, Paris, London, and Berlin. "
            "Captain Price and Yuri hunt Vladimir Makarov to Dubai for the climactic final showdown: 'For Soap'."
        ),
        "specs": {
            "min_os": "Windows XP / Vista / 7 / 10",
            "min_cpu": "Intel Core 2 Duo E6600 / AMD Phenom X3 8750",
            "min_ram": "2 GB",
            "min_gpu": "NVIDIA GeForce 8600GT / ATI Radeon X1950",
            "rec_os": "Windows 10",
            "rec_cpu": "Intel Core i5-2400",
            "rec_ram": "4 GB",
            "rec_gpu": "NVIDIA GeForce GTX 560"
        },
        "achievements": [
            {"id": "mw3_orig_01", "name": "Back in the Fight", "desc": "Start the Single Player Campaign on any difficulty.", "unlocked": True, "icon": "shield"},
            {"id": "mw3_orig_02", "name": "For Soap", "desc": "Eliminate Makarov in the Hotel Oasis.", "unlocked": True, "icon": "skull"},
            {"id": "mw3_orig_03", "name": "Survivor", "desc": "Reach Wave 15 in each mission of Special Ops Survival mode.", "unlocked": True, "icon": "medal"}
        ]
    },
    "cod-bo1": {
        "id": "cod-bo1",
        "title": "Call of Duty: Black Ops (2010)",
        "subtitle": "The Numbers, Mason! What Do They Mean?",
        "release_year": 2010,
        "release_date": "November 9, 2010",
        "series": "Black Ops",
        "developer": "Treyarch",
        "publisher": "Activision",
        "engine": "IW 3.0 Modified",
        "steam_appid": 42700,
        "battlenet_id": "",
        "default_exes": ["BlackOps.exe", "BlackOpsMP.exe"],
        "default_dirs": ["Call of Duty Black Ops"],
        "modes": ["Campaign", "Multiplayer (Wager Matches)", "Kino Der Toten & Moon Zombies", "Dead Ops Arcade"],
        "storage_gb": 12,
        "is_installed": True,
        "installed_path": "C:\\Program Files (x86)\\Steam\\steamapps\\common\\Call of Duty Black Ops\\BlackOps.exe",
        "install_platform": "Steam",
        "playtime_hours": 195.4,
        "last_played": "May 2024",
        "is_favorite": True,
        "launch_args": "",
        "synopsis": (
            "Alex Mason awakens strapped to an interrogation chair in an enigmatic facility. Relive covert operations "
            "in Cuba, Vietnam, Laos, and Russia to stop General Dragovich, Kravchenko, and Steiner's Nova 6 gas."
        ),
        "specs": {
            "min_os": "Windows Vista / XP / 7 / 10",
            "min_cpu": "Intel Core 2 Duo E6600 / AMD Phenom X3 8750",
            "min_ram": "2 GB",
            "min_gpu": "Shader 3.0 or better 256MB NVIDIA GeForce 8600GT / ATI Radeon X1950Pro",
            "rec_os": "Windows 10",
            "rec_cpu": "Intel Core i5-2500K",
            "rec_ram": "4 GB",
            "rec_gpu": "NVIDIA GeForce GTX 460"
        },
        "achievements": [
            {"id": "bo1_01", "name": "The Big Gamble", "desc": "Win 5 Wager Matches in Multiplayer.", "unlocked": True, "icon": "target"},
            {"id": "bo1_02", "name": "Vorkuta Revolutionary", "desc": "Escape Vorkuta labor camp with Viktor Reznov.", "unlocked": True, "icon": "shield"},
            {"id": "bo1_03", "name": "One Giant Leap", "desc": "Launch the rockets from the Moon in Zombies.", "unlocked": True, "icon": "skull"}
        ]
    },
    "cod-mw2-2009": {
        "id": "cod-mw2-2009",
        "title": "Call of Duty: Modern Warfare 2 (2009)",
        "subtitle": "The Benchmark of Modern Shooters // Task Force 141",
        "release_year": 2009,
        "release_date": "November 10, 2009",
        "series": "Modern Warfare",
        "developer": "Infinity Ward",
        "publisher": "Activision",
        "engine": "IW 4.0",
        "steam_appid": 10180,
        "battlenet_id": "",
        "default_exes": ["iw4sp.exe", "iw4mp.exe"],
        "default_dirs": ["Call of Duty Modern Warfare 2", "Modern Warfare 2"],
        "modes": ["Campaign", "Multiplayer", "Special Ops"],
        "storage_gb": 12,
        "is_installed": True,
        "installed_path": "C:\\Program Files (x86)\\Steam\\steamapps\\common\\Call of Duty Modern Warfare 2\\iw4sp.exe",
        "install_platform": "Steam",
        "playtime_hours": 512.6,
        "last_played": "Last month",
        "is_favorite": True,
        "launch_args": "",
        "synopsis": (
            "The ground-breaking blockbuster that defined an era. Task Force 141 and the US Army Rangers battle across "
            "Rio de Janeiro, the Boneyard, Gulag, and Washington D.C. Features legendary Spec Ops and unmatched multiplayer."
        ),
        "specs": {
            "min_os": "Windows XP / Vista / 7 / 10",
            "min_cpu": "Intel Pentium 4 3.2 GHz or AMD Athlon 64 3200+",
            "min_ram": "1 GB",
            "min_gpu": "256 MB NVIDIA GeForce 6600GT or ATI Radeon 1600XT",
            "rec_os": "Windows 10",
            "rec_cpu": "Intel Core 2 Duo",
            "rec_ram": "2 GB",
            "rec_gpu": "NVIDIA GeForce 8800GT"
        },
        "achievements": [
            {"id": "mw2_orig_01", "name": "Back in the Saddle", "desc": "Help train the local militia.", "unlocked": True, "icon": "shield"},
            {"id": "mw2_orig_02", "name": "The Price of War", "desc": "Complete the Campaign on Veteran.", "unlocked": True, "icon": "medal"},
            {"id": "mw2_orig_03", "name": "Star 69", "desc": "Earn all 69 stars in Special Ops.", "unlocked": True, "icon": "star"},
            {"id": "mw2_orig_04", "name": "Tactical Nuke", "desc": "Call in a Tactical Nuke in Multiplayer.", "unlocked": True, "icon": "hazard"}
        ]
    },
    "cod-waw": {
        "id": "cod-waw",
        "title": "Call of Duty: World at War",
        "subtitle": "The Brutal Pacific & Eastern Fronts // Birth of Zombies",
        "release_year": 2008,
        "release_date": "November 11, 2008",
        "series": "World War II",
        "developer": "Treyarch",
        "publisher": "Activision",
        "engine": "IW 3.0 Modified",
        "steam_appid": 10090,
        "battlenet_id": "",
        "default_exes": ["CoDWaW.exe", "CoDWaWmp.exe"],
        "default_dirs": ["Call of Duty World at War"],
        "modes": ["Campaign (Co-op)", "Multiplayer", "Nazi Zombies (Nacht der Untoten, Der Riese)"],
        "storage_gb": 8,
        "is_installed": True,
        "installed_path": "C:\\Program Files (x86)\\Steam\\steamapps\\common\\Call of Duty World at War\\CoDWaW.exe",
        "install_platform": "Steam",
        "playtime_hours": 140.0,
        "last_played": "2023",
        "is_favorite": True,
        "launch_args": "",
        "synopsis": (
            "Experience the gritty realism of WWII through Marine Raider Miller in the Pacific against Imperial Japan "
            "and Red Army soldier Dimitri Petrenko under Sgt. Viktor Reznov storming the Reichstag. Introduces Nazi Zombies."
        ),
        "specs": {
            "min_os": "Windows XP / Vista / 7 / 10",
            "min_cpu": "AMD 64 3200+ / Intel Pentium 4 3.0GHz",
            "min_ram": "512 MB (XP) / 1 GB (Vista)",
            "min_gpu": "NVIDIA GeForce 6600GT / ATI Radeon X1600",
            "rec_os": "Windows 10",
            "rec_cpu": "Intel Core 2 Duo",
            "rec_ram": "2 GB",
            "rec_gpu": "NVIDIA GeForce 8800GT"
        },
        "achievements": [
            {"id": "waw_01", "name": "The Reichstag Flag", "desc": "Plant the Soviet flag atop the Reichstag.", "unlocked": True, "icon": "shield"},
            {"id": "waw_02", "name": "Der Riese Overlord", "desc": "Pack-a-Punch your first weapon in Der Riese.", "unlocked": True, "icon": "skull"},
            {"id": "waw_03", "name": "Heart of the Reich", "desc": "Survive the 88mm battery assault on Veteran.", "unlocked": False, "icon": "medal"}
        ]
    },
    "cod-cod4": {
        "id": "cod-cod4",
        "title": "Call of Duty 4: Modern Warfare (2007)",
        "subtitle": "The Masterpiece That Changed Gaming Forever",
        "release_year": 2007,
        "release_date": "November 5, 2007",
        "series": "Modern Warfare",
        "developer": "Infinity Ward",
        "publisher": "Activision",
        "engine": "IW 3.0",
        "steam_appid": 7940,
        "battlenet_id": "",
        "default_exes": ["iw3sp.exe", "iw3mp.exe"],
        "default_dirs": ["Call of Duty 4 Modern Warfare", "Call of Duty 4"],
        "modes": ["Campaign", "Multiplayer", "Arcade Mode"],
        "storage_gb": 8,
        "is_installed": True,
        "installed_path": "C:\\Program Files (x86)\\Steam\\steamapps\\common\\Call of Duty 4\\iw3sp.exe",
        "install_platform": "Steam",
        "playtime_hours": 320.0,
        "last_played": "2024",
        "is_favorite": True,
        "launch_args": "",
        "synopsis": (
            "The genre-defining classic. Join the British SAS under Captain Price and US Marine Sgt. Paul Jackson. "
            "Featuring iconic missions like 'All Ghillied Up' in Pripyat, 'Death From Above', and 'War Pig'."
        ),
        "specs": {
            "min_os": "Windows XP / Vista / 7 / 10",
            "min_cpu": "Intel Pentium 4 2.4 GHz / AMD(R) 64 (TM) 2800+",
            "min_ram": "512 MB (XP) / 768 MB (Vista)",
            "min_gpu": "NVIDIA Geforce 6600 / ATI Radeon 9800Pro",
            "rec_os": "Windows 10",
            "rec_cpu": "2.4 GHz dual core or better",
            "rec_ram": "2 GB",
            "rec_gpu": "NVIDIA Geforce 7800 / ATI Radeon X1800"
        },
        "achievements": [
            {"id": "cod4_01", "name": "All Ghillied Up", "desc": "Sneak past the Russian patrols without alerting guards.", "unlocked": True, "icon": "target"},
            {"id": "cod4_02", "name": "Death from Above", "desc": "Provide air support from the AC-130 gunship.", "unlocked": True, "icon": "shield"},
            {"id": "cod4_03", "name": "Deep and Hard", "desc": "Complete the Campaign on Veteran.", "unlocked": True, "icon": "medal"}
        ]
    },
    "cod3": {
        "id": "cod3",
        "title": "Call of Duty 3",
        "subtitle": "The Battle for Normandy // Allied Coalition",
        "release_year": 2006,
        "release_date": "November 7, 2006",
        "series": "Classic Era",
        "developer": "Treyarch",
        "publisher": "Activision",
        "engine": "Treyarch NGL Engine",
        "steam_appid": 0,
        "battlenet_id": "",
        "default_exes": [],
        "default_dirs": [],
        "modes": ["Campaign", "Allied Multiplayer with Vehicles"],
        "storage_gb": 6,
        "is_installed": False,
        "installed_path": "",
        "install_platform": "Console Classic (Intel Archive)",
        "playtime_hours": 24.0,
        "last_played": "Archived",
        "is_favorite": False,
        "launch_args": "",
        "synopsis": (
            "Experience the breakout from Normandy in the Falaise Pocket through four Allied campaigns: "
            "American, British, Canadian, and Polish armored forces fighting side-by-side."
        ),
        "specs": {
            "min_os": "Console Historic Release (Xbox 360 / PS3)",
            "min_cpu": "Tri-Core PowerPC",
            "min_ram": "512 MB",
            "min_gpu": "ATI Xenos / RSX",
            "rec_os": "Windows PC via Preservation Archive",
            "rec_cpu": "Quad Core x86_64",
            "rec_ram": "8 GB",
            "rec_gpu": "GTX 1060"
        },
        "achievements": [
            {"id": "cod3_01", "name": "Falaise Pocket", "desc": "Survive the Chambois encirclement.", "unlocked": True, "icon": "shield"},
            {"id": "cod3_02", "name": "Polish Armor", "desc": "Defend Hill 262 against German Panzer divisions.", "unlocked": False, "icon": "star"}
        ]
    },
    "cod2": {
        "id": "cod2",
        "title": "Call of Duty 2",
        "subtitle": "No One Fights Alone // Redefining Second Generation Combat",
        "release_year": 2005,
        "release_date": "October 25, 2005",
        "series": "Classic Era",
        "developer": "Infinity Ward",
        "publisher": "Activision",
        "engine": "IW 2.0",
        "steam_appid": 2610,
        "battlenet_id": "",
        "default_exes": ["cod2sp.exe", "cod2mp.exe"],
        "default_dirs": ["Call of Duty 2"],
        "modes": ["Campaign", "Multiplayer"],
        "storage_gb": 4,
        "is_installed": True,
        "installed_path": "C:\\Program Files (x86)\\Steam\\steamapps\\common\\Call of Duty 2\\cod2sp.exe",
        "install_platform": "Steam",
        "playtime_hours": 62.0,
        "last_played": "2023",
        "is_favorite": True,
        "launch_args": "",
        "synopsis": (
            "Pioneered regenerating health, grenade indicators, and squad warfare. Play as Soviet soldier Vasili Ivanovich Koslov "
            "in Stalingrad, British Sgt. John Davis in North Africa, and US Army Ranger Corporal Bill Taylor scaling Pointe du Hoc on D-Day."
        ),
        "specs": {
            "min_os": "Windows 2000 / XP / 7 / 10",
            "min_cpu": "Pentium IV 1.4GHz or AMD Athlon XP 1700+",
            "min_ram": "256 MB",
            "min_gpu": "64 MB DirectX 9.0c compliant hardware video card",
            "rec_os": "Windows 10",
            "rec_cpu": "2.8 GHz",
            "rec_ram": "1 GB",
            "rec_gpu": "GeForce 6800 or Radeon X800"
        },
        "achievements": [
            {"id": "cod2_01", "name": "Pointe du Hoc", "desc": "Scale the cliffs of Pointe du Hoc under intense machine gun fire.", "unlocked": True, "icon": "shield"},
            {"id": "cod2_02", "name": "Stalingrad Defender", "desc": "Complete the Soviet campaign on Veteran.", "unlocked": True, "icon": "medal"},
            {"id": "cod2_03", "name": "Desert Fox Hunter", "desc": "Drive Rommel out of El Alamein.", "unlocked": True, "icon": "target"}
        ]
    },
    "cod-uo": {
        "id": "cod-uo",
        "title": "Call of Duty: United Offensive",
        "subtitle": "The Legendary Expansion // Battle of the Bulge",
        "release_year": 2004,
        "release_date": "September 14, 2004",
        "series": "Classic Era",
        "developer": "Gray Matter Studios / Treyarch",
        "publisher": "Activision",
        "engine": "id Tech 3 Modified",
        "steam_appid": 2630,
        "battlenet_id": "",
        "default_exes": ["CoDUOSP.exe", "CoDUOMP.exe"],
        "default_dirs": ["Call of Duty", "Call of Duty United Offensive"],
        "modes": ["Campaign", "Multiplayer with Tanks & Jeeps (Base Assault)"],
        "storage_gb": 3,
        "is_installed": True,
        "installed_path": "C:\\Program Files (x86)\\Steam\\steamapps\\common\\Call of Duty\\CoDUOSP.exe",
        "install_platform": "Steam",
        "playtime_hours": 38.0,
        "last_played": "2022",
        "is_favorite": False,
        "launch_args": "",
        "synopsis": (
            "Expanded the original Call of Duty with massive scale: B-17 Flying Fortress bomber gunner missions, "
            "the Battle of Kursk tank clashes, and winter fighting in the Ardennes during the Battle of the Bulge."
        ),
        "specs": {
            "min_os": "Windows 98 / ME / 2000 / XP / 10",
            "min_cpu": "Pentium III 800MHz or Athlon 800MHz",
            "min_ram": "128 MB",
            "min_gpu": "32 MB 100% DirectX 9.0b compliant hardware card",
            "rec_os": "Windows 10",
            "rec_cpu": "1.5 GHz",
            "rec_ram": "512 MB",
            "rec_gpu": "GeForce 4 Ti or Radeon 9500"
        },
        "achievements": [
            {"id": "uo_01", "name": "B-17 Top Gun", "desc": "Shoot down 20 German fighters over Rotterdam.", "unlocked": True, "icon": "target"},
            {"id": "uo_02", "name": "Kursk Victory", "desc": "Command the T-34 tank division to victory at Ponyri.", "unlocked": True, "icon": "shield"}
        ]
    },
    "cod1": {
        "id": "cod1",
        "title": "Call of Duty (2003)",
        "subtitle": "In the War That Changed the World, No One Fought Alone",
        "release_year": 2003,
        "release_date": "October 29, 2003",
        "series": "Classic Era",
        "developer": "Infinity Ward",
        "publisher": "Activision",
        "engine": "id Tech 3 (Modified)",
        "steam_appid": 2620,
        "battlenet_id": "",
        "default_exes": ["CoDSP.exe", "CoDMP.exe"],
        "default_dirs": ["Call of Duty"],
        "modes": ["Campaign", "Multiplayer"],
        "storage_gb": 2,
        "is_installed": True,
        "installed_path": "C:\\Program Files (x86)\\Steam\\steamapps\\common\\Call of Duty\\CoDSP.exe",
        "install_platform": "Steam",
        "playtime_hours": 45.0,
        "last_played": "2023",
        "is_favorite": True,
        "launch_args": "",
        "synopsis": (
            "The historic beginning of the franchise. Game of the Year 2003 winner created by former Medal of Honor Allied Assault "
            "veterans. Follow Private Martin (US 101st Airborne), Sgt. Evans (British 6th Airborne Division Pegasus Bridge), and Alexei (Red Army)."
        ),
        "specs": {
            "min_os": "Windows 98 / ME / 2000 / XP / 10",
            "min_cpu": "Pentium III 600MHz or Athlon 600MHz",
            "min_ram": "128 MB",
            "min_gpu": "32 MB DirectX 9.0b hardware T&L video card",
            "rec_os": "Windows 10",
            "rec_cpu": "1.0 GHz",
            "rec_ram": "256 MB",
            "rec_gpu": "GeForce 3 or Radeon 8500"
        },
        "achievements": [
            {"id": "cod1_01", "name": "Pegasus Bridge", "desc": "Capture and hold the Benouville bridge in Normandy.", "unlocked": True, "icon": "shield"},
            {"id": "cod1_02", "name": "Red Square Storm", "desc": "Cross the Volga river and reach the department store.", "unlocked": True, "icon": "star"},
            {"id": "cod1_03", "name": "War Over", "desc": "Raise the Victory banner over the Reichstag.", "unlocked": True, "icon": "medal"}
        ]
    }
}

SERIES_CATEGORIES = [
    "ALL",
    "Modern Warfare",
    "Black Ops",
    "World War II",
    "Advanced & Futuristic",
    "Classic Era",
    "Warzone"
]

def get_all_games() -> List[Dict[str, Any]]:
    """Return all games ordered chronologically (newest first)."""
    games = list(GAMES_DATABASE.values())
    games.sort(key=lambda g: (g["release_year"], g.get("release_date", "")), reverse=True)
    return games

def get_game_by_id(game_id: str) -> Dict[str, Any] | None:
    return GAMES_DATABASE.get(game_id)
