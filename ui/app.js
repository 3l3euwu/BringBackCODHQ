/* ==========================================================================
   CALL OF DUTY // HQ LAUNCHER - CLIENT APPLICATION CONTROLLER
   Full tactical desktop operations controller, PC auto-detection manager,
   Steam synchronization, and audio synthesizer.
   ========================================================================== */

class CodHQApp {
    constructor() {
        this.games = [];
        this.featuredGameId = "cod-bo6";
        this.currentTab = "overview";
        this.seriesFilter = "ALL";
        this.searchQuery = "";
        this.statusFilter = "all";
        this.sortOrder = "year_desc";
        this.soundEnabled = true;
        this.audioCtx = null;
        this.steamProfile = null;
        this.detectedScanGames = [];
        this.currentModalGame = null;
        this.selectedAchGameId = "cod-bo6";

        this.init();
    }

    async init() {
        this.initAudio();
        this.initClock();
        this.loadSettings();
        await this.fetchGames();
        await this.fetchSteamProfile();
        this.renderOverview();
        this.renderLibrary();
        this.renderAchievementsShowcase();
    }

    /* ==========================================================================
       TACTICAL AUDIO SYNTHESIZER (WEB AUDIO API)
       Zero external audio files needed; authentic military clicks & deploy SFX.
       ========================================================================== */

    initAudio() {
        const saved = localStorage.getItem("cod_hq_sound");
        if (saved !== null) {
            this.soundEnabled = saved === "true";
        }
        this.updateAudioUI();
    }

    ensureAudioContext() {
        if (!this.audioCtx) {
            const AudioContext = window.AudioContext || window.webkitAudioContext;
            this.audioCtx = new AudioContext();
        }
        if (this.audioCtx.state === "suspended") {
            this.audioCtx.resume();
        }
    }

    playClick() {
        if (!this.soundEnabled) return;
        try {
            this.ensureAudioContext();
            const osc = this.audioCtx.createOscillator();
            const gain = this.audioCtx.createGain();
            const now = this.audioCtx.currentTime;

            osc.type = "sine";
            osc.frequency.setValueAtTime(1400, now);
            osc.frequency.exponentialRampToValueAtTime(400, now + 0.035);

            gain.gain.setValueAtTime(0.12, now);
            gain.gain.exponentialRampToValueAtTime(0.001, now + 0.035);

            osc.connect(gain);
            gain.connect(this.audioCtx.destination);

            osc.start(now);
            osc.stop(now + 0.04);
        } catch (e) {
            // Audio error suppressed
        }
    }

    playDeploy() {
        if (!this.soundEnabled) return;
        try {
            this.ensureAudioContext();
            const now = this.audioCtx.currentTime;

            // 1. Sub-bass punch
            const osc = this.audioCtx.createOscillator();
            const gain = this.audioCtx.createGain();
            osc.type = "sawtooth";
            osc.frequency.setValueAtTime(110, now);
            osc.frequency.exponentialRampToValueAtTime(32, now + 0.3);

            gain.gain.setValueAtTime(0.25, now);
            gain.gain.exponentialRampToValueAtTime(0.001, now + 0.35);

            osc.connect(gain);
            gain.connect(this.audioCtx.destination);
            osc.start(now);
            osc.stop(now + 0.35);

            // 2. Tactical radio chirp
            const chirp = this.audioCtx.createOscillator();
            const chirpGain = this.audioCtx.createGain();
            chirp.type = "sine";
            chirp.frequency.setValueAtTime(1800, now + 0.05);
            chirp.frequency.exponentialRampToValueAtTime(900, now + 0.12);

            chirpGain.gain.setValueAtTime(0.08, now + 0.05);
            chirpGain.gain.exponentialRampToValueAtTime(0.001, now + 0.12);

            chirp.connect(chirpGain);
            chirpGain.connect(this.audioCtx.destination);
            chirp.start(now + 0.05);
            chirp.stop(now + 0.13);
        } catch (e) {
            // Audio error suppressed
        }
    }

    playRadarPing() {
        if (!this.soundEnabled) return;
        try {
            this.ensureAudioContext();
            const now = this.audioCtx.currentTime;
            const osc = this.audioCtx.createOscillator();
            const gain = this.audioCtx.createGain();

            osc.type = "triangle";
            osc.frequency.setValueAtTime(2200, now);
            osc.frequency.exponentialRampToValueAtTime(1200, now + 0.08);

            gain.gain.setValueAtTime(0.09, now);
            gain.gain.exponentialRampToValueAtTime(0.001, now + 0.08);

            osc.connect(gain);
            gain.connect(this.audioCtx.destination);
            osc.start(now);
            osc.stop(now + 0.09);
        } catch (e) {
            // Suppress
        }
    }

    toggleAudio() {
        this.soundEnabled = !this.soundEnabled;
        localStorage.setItem("cod_hq_sound", this.soundEnabled);
        this.updateAudioUI();
        if (this.soundEnabled) {
            this.playClick();
            this.toast("TACTICAL AUDIO FEEDBACK: ACTIVATED");
        } else {
            this.toast("TACTICAL AUDIO FEEDBACK: MUTED");
        }
    }

    updateAudioUI() {
        const icon = document.getElementById("audioIcon");
        const label = document.getElementById("audioLabel");
        const settingChk = document.getElementById("settingAudioToggle");

        if (this.soundEnabled) {
            if (icon) icon.innerText = "🔊";
            if (label) label.innerText = "SFX: ON";
            if (settingChk) settingChk.checked = true;
        } else {
            if (icon) icon.innerText = "🔇";
            if (label) label.innerText = "SFX: MUTED";
            if (settingChk) settingChk.checked = false;
        }
    }

    /* ==========================================================================
       CLOCK & SETTINGS
       ========================================================================== */

    initClock() {
        const update = () => {
            const el = document.getElementById("tacticalClock");
            if (el) {
                const now = new Date();
                const h = String(now.getUTCHours()).padStart(2, "0");
                const m = String(now.getUTCMinutes()).padStart(2, "0");
                const s = String(now.getUTCSeconds()).padStart(2, "0");
                el.innerText = `${h}:${m}:${s}Z (UTC)`;
            }
        };
        update();
        setInterval(update, 1000);
    }

    loadSettings() {
        const theme = localStorage.getItem("cod_hq_theme") || "theme-olive";
        this.setTheme(theme, false);
    }

    setTheme(themeName, notify = true) {
        document.body.className = themeName;
        localStorage.setItem("cod_hq_theme", themeName);

        document.querySelectorAll(".theme-option").forEach(opt => {
            opt.classList.toggle("active", opt.dataset.theme === themeName);
        });

        if (notify) {
            this.playClick();
            const names = {
                "theme-olive": "TACTICAL OLIVE DRAB",
                "theme-sand": "DESERT SAND & KHAKI",
                "theme-night": "NIGHT OPS STEALTH CAMO"
            };
            this.toast(`VISUAL THEME UPDATED: ${names[themeName] || themeName}`);
        }
    }

    /* ==========================================================================
       NAVIGATION & TABS
       ========================================================================== */

    setTab(tabId) {
        this.playClick();
        this.currentTab = tabId;

        document.querySelectorAll(".nav-tab").forEach(tab => {
            tab.classList.toggle("active", tab.dataset.tab === tabId);
        });

        document.querySelectorAll(".view-tab").forEach(view => {
            view.classList.toggle("active", view.id === `tab-${tabId}`);
        });

        window.scrollTo({ top: 0, behavior: "smooth" });

        if (tabId === "scanner" && this.detectedScanGames.length === 0) {
            this.triggerScan(false);
        }
    }

    /* ==========================================================================
       API & DATA MANAGEMENT
       ========================================================================== */

    async fetchGames() {
        try {
            const res = await fetch("/api/games");
            if (res.ok) {
                this.games = await res.json();
                this.updateTickers();
            }
        } catch (e) {
            console.error("Failed to fetch games:", e);
        }
    }

    async fetchSteamProfile() {
        try {
            const res = await fetch("/api/steam/profile");
            if (res.ok) {
                this.steamProfile = await res.json();
                this.renderSteamProfileHeader();
            }
        } catch (e) {
            console.error("Failed to fetch Steam profile:", e);
        }
    }

    updateTickers() {
        const total = this.games.length;
        const installed = this.games.filter(g => g.is_installed).length;
        const totalHours = this.games.reduce((acc, g) => acc + (g.playtime_hours || 0), 0);

        const tTotal = document.getElementById("tickerTotalGames");
        if (tTotal) tTotal.innerText = `${total} REGISTERED`;

        const tInst = document.getElementById("tickerInstalledGames");
        if (tInst) tInst.innerText = `${installed} COMBAT READY`;

        const tHours = document.getElementById("tickerPlaytime");
        if (tHours) tHours.innerText = `${totalHours.toFixed(1)} HRS`;
    }

    /* ==========================================================================
       RENDERING: HQ OVERVIEW & SPOTLIGHT
       ========================================================================== */

    renderOverview() {
        const featured = this.games.find(g => g.id === this.featuredGameId) || this.games[0];
        if (!featured) return;

        const backdrop = document.getElementById("heroBackdrop");
        if (backdrop) {
            backdrop.style.backgroundImage = `url('/assets/banners/${featured.id}.jpg')`;
        }

        const title = document.getElementById("heroTitle");
        if (title) title.innerText = featured.title;

        const sub = document.getElementById("heroSubtitle");
        if (sub) sub.innerText = featured.subtitle;

        const syn = document.getElementById("heroSynopsis");
        if (syn) syn.innerText = featured.synopsis;

        const sBadge = document.getElementById("heroSeriesBadge");
        if (sBadge) sBadge.innerText = featured.series.toUpperCase();

        const yBadge = document.getElementById("heroYearBadge");
        if (yBadge) yBadge.innerText = `${featured.release_year} DEPLOYMENT`;

        const stBadge = document.getElementById("heroStatusBadge");
        if (stBadge) {
            stBadge.innerText = featured.is_installed ? "READY FOR COMBAT" : "AVAILABLE TO INSTALL";
            stBadge.style.color = featured.is_installed ? "var(--accent)" : "var(--accent-sand)";
        }

        const pTime = document.getElementById("heroPlaytime");
        if (pTime) pTime.innerText = `${featured.playtime_hours || 0} HRS`;

        const pStorage = document.getElementById("heroStorage");
        if (pStorage) pStorage.innerText = `${featured.storage_gb || 80} GB SSD`;

        const pPlat = document.getElementById("heroPlatform");
        if (pPlat) pPlat.innerText = `${featured.install_platform || "PC"} CLIENT`;

        // Achievements count
        const ach = featured.achievements || [];
        const unlocked = ach.filter(a => a.unlocked).length;
        const pct = ach.length ? Math.round((unlocked / ach.length) * 100) : 0;
        const pAch = document.getElementById("heroAchievements");
        if (pAch) pAch.innerText = `${unlocked} / ${ach.length} UNLOCKED (${pct}%)`;

        // Render Quick Deploy row (Installed / Favorites)
        this.renderQuickDeployGrid();
    }

    renderQuickDeployGrid() {
        const container = document.getElementById("quickDeployGrid");
        if (!container) return;

        const installedGames = this.games.filter(g => g.is_installed || g.is_favorite).slice(0, 6);

        container.innerHTML = installedGames.map(game => `
            <div class="quick-card" onclick="app.openDossier('${game.id}')">
                <img src="/assets/covers/${game.id}.jpg" alt="${game.title}" class="quick-cover" onerror="this.src='/assets/icons/cod_hq.png'">
                <div class="quick-info">
                    <div class="quick-title">${game.title}</div>
                    <div class="quick-sub">${game.series} // ${game.release_year}</div>
                    <div class="quick-hours">SERVICE: ${game.playtime_hours || 0} HRS</div>
                </div>
                <button class="quick-btn-deploy" onclick="event.stopPropagation(); app.launchGame('${game.id}', 'default')">
                    DEPLOY
                </button>
            </div>
        `).join("");
    }

    /* ==========================================================================
       RENDERING: FRANCHISE LIBRARY
       ========================================================================== */

    setSeriesFilter(series) {
        this.playClick();
        this.seriesFilter = series;

        document.querySelectorAll("#seriesFilterGroup .filter-pill").forEach(pill => {
            pill.classList.toggle("active", pill.dataset.series === series);
        });

        this.renderLibrary();
    }

    filterBySeries(series) {
        this.setTab("library");
        this.setSeriesFilter(series);
    }

    onSearchInput() {
        const input = document.getElementById("gameSearchInput");
        this.searchQuery = input ? input.value.trim().toLowerCase() : "";
        this.renderLibrary();
    }

    clearSearch() {
        const input = document.getElementById("gameSearchInput");
        if (input) input.value = "";
        this.searchQuery = "";
        this.renderLibrary();
    }

    renderLibrary() {
        const grid = document.getElementById("gamesGrid");
        if (!grid) return;

        const statusSel = document.getElementById("statusFilter");
        this.statusFilter = statusSel ? statusSel.value : "all";

        const sortSel = document.getElementById("sortOrder");
        this.sortOrder = sortSel ? sortSel.value : "year_desc";

        // Filter
        let filtered = [...this.games];

        if (this.seriesFilter !== "ALL") {
            filtered = filtered.filter(g => g.series === this.seriesFilter);
        }

        if (this.statusFilter === "installed") {
            filtered = filtered.filter(g => g.is_installed);
        } else if (this.statusFilter === "favorites") {
            filtered = filtered.filter(g => g.is_favorite);
        } else if (this.statusFilter === "uninstalled") {
            filtered = filtered.filter(g => !g.is_installed);
        }

        if (this.searchQuery) {
            filtered = filtered.filter(g => 
                g.title.toLowerCase().includes(this.searchQuery) ||
                g.subtitle.toLowerCase().includes(this.searchQuery) ||
                String(g.release_year).includes(this.searchQuery) ||
                g.developer.toLowerCase().includes(this.searchQuery)
            );
        }

        // Sort
        if (this.sortOrder === "year_desc") {
            filtered.sort((a, b) => b.release_year - a.release_year);
        } else if (this.sortOrder === "year_asc") {
            filtered.sort((a, b) => a.release_year - b.release_year);
        } else if (this.sortOrder === "playtime_desc") {
            filtered.sort((a, b) => (b.playtime_hours || 0) - (a.playtime_hours || 0));
        } else if (this.sortOrder === "title_asc") {
            filtered.sort((a, b) => a.title.localeCompare(b.title));
        }

        if (filtered.length === 0) {
            grid.innerHTML = `
                <div style="grid-column: 1/-1; text-align: center; padding: 60px 20px; color: var(--text-muted); font-family: var(--font-mono);">
                    NO CALL OF DUTY RELEASES MATCH CURRENT TACTICAL FILTERS.
                </div>
            `;
            return;
        }

        grid.innerHTML = filtered.map(game => {
            const ledClass = game.is_installed ? "status-installed" : "status-uninstalled";
            return `
                <div class="game-card" onclick="app.openDossier('${game.id}')">
                    <div class="card-cover-wrap">
                        <img src="/assets/covers/${game.id}.jpg" alt="${game.title}" class="card-cover-img" onerror="this.src='/assets/icons/cod_hq.png'">
                        <div class="card-badges-top">
                            <span class="card-badge-year">${game.release_year}</span>
                            <div class="card-led-status ${ledClass}" title="${game.is_installed ? 'Installed & Ready' : 'Uninstalled'}"></div>
                        </div>

                        <!-- Hover Overlay -->
                        <div class="card-hover-overlay">
                            <span style="font-family: var(--font-heading); font-size: 16px; color: #fff; text-transform: uppercase;">${game.title}</span>
                            <button class="btn-deploy" style="padding: 8px 18px; font-size: 13px;" onclick="event.stopPropagation(); app.launchGame('${game.id}', 'default')">
                                DEPLOY
                            </button>
                            <button class="btn-tactical-sm" style="padding: 6px 14px;" onclick="event.stopPropagation(); app.openDossier('${game.id}')">
                                INTEL DOSSIER
                            </button>
                        </div>
                    </div>

                    <div class="card-meta-bottom">
                        <div class="card-title">${game.title}</div>
                        <span class="card-series-tag">${game.series.toUpperCase()}</span>
                        <div class="card-footer-stats">
                            <span>SERVICE: ${game.playtime_hours ? game.playtime_hours + ' HRS' : '--'}</span>
                            <span>${game.install_platform}</span>
                        </div>
                    </div>
                </div>
            `;
        }).join("");
    }

    /* ==========================================================================
       PC AUTO-LOCATE SCANNER
       ========================================================================== */

    async triggerScan(notify = true) {
        this.playClick();
        const sweep = document.getElementById("radarSweep");
        const statusText = document.getElementById("radarStatusText");
        const summary = document.getElementById("scanResultsSummary");
        const startBtn = document.getElementById("startScanBtn");

        if (sweep) sweep.classList.add("scanning");
        if (statusText) statusText.innerText = "SCANNING DRIVES...";
        if (summary) summary.innerText = "DEEP SCAN IN PROGRESS // PARSING STEAM & BATTLE.NET...";
        if (startBtn) startBtn.disabled = true;

        this.playRadarPing();

        try {
            const res = await fetch("/api/scan", { method: "POST" });
            if (res.ok) {
                const data = await res.json();
                this.detectedScanGames = data.games || [];
                this.renderScannerTable();

                if (statusText) statusText.innerText = `ONLINE // ${data.games_detected_count} DETECTED`;
                if (summary) {
                    summary.innerText = `COMPLETE // ${data.games_detected_count} CALL OF DUTY RELEASES IDENTIFIED`;
                }

                const badge = document.getElementById("scannerBadge");
                if (badge) badge.innerText = `${data.games_detected_count} DETECTED`;

                if (notify) {
                    this.toast(`PC SCAN COMPLETE: ${data.games_detected_count} COD TITLES IDENTIFIED`);
                }
            }
        } catch (e) {
            console.error("Scan error:", e);
        } finally {
            if (sweep) sweep.classList.remove("scanning");
            if (startBtn) startBtn.disabled = false;
        }
    }

    async scanCustomDir() {
        const input = document.getElementById("customDirInput");
        const path = input ? input.value.trim() : "";
        if (!path) {
            this.toast("PLEASE SPECIFY A FOLDER PATH TO SCAN");
            return;
        }

        this.toast(`SCANNING CUSTOM DIRECTORY: ${path}`);
        this.playClick();

        try {
            const res = await fetch("/api/scan", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ custom_dirs: [path] })
            });

            if (res.ok) {
                const data = await res.json();
                this.detectedScanGames = data.games || [];
                this.renderScannerTable();
                this.toast(`SCAN COMPLETE // FOUND ${data.games_detected_count} TITLES`);
            }
        } catch (e) {
            console.error("Custom scan error:", e);
        }
    }

    renderScannerTable() {
        const tbody = document.getElementById("detectedTableBody");
        if (!tbody) return;

        if (this.detectedScanGames.length === 0) {
            tbody.innerHTML = `
                <tr>
                    <td colspan="6" style="text-align: center; color: var(--text-muted); padding: 30px;">
                        NO GAMES DETECTED YET. CLICK "INITIATE DEEP PC SCAN".
                    </td>
                </tr>
            `;
            return;
        }

        tbody.innerHTML = this.detectedScanGames.map(item => `
            <tr>
                <td style="font-weight: 700; color: #fff;">${item.title}</td>
                <td><span class="setting-pill">${item.platform}</span></td>
                <td style="color: var(--accent-sand); font-size: 11px;">${item.installed_path}</td>
                <td>${item.size_gb} GB</td>
                <td style="color: var(--accent);">COMBAT READY</td>
                <td>
                    <button class="btn-tactical-sm" onclick="app.launchGame('${item.game_id}', 'default')">
                        DEPLOY
                    </button>
                </td>
            </tr>
        `).join("");
    }

    async applyAllDetected() {
        this.playClick();
        if (this.detectedScanGames.length === 0) {
            this.toast("NO SCANNED TITLES TO APPLY. RUN SCAN FIRST.");
            return;
        }

        try {
            const res = await fetch("/api/scan/apply", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ detected_games: this.detectedScanGames })
            });

            if (res.ok) {
                const data = await res.json();
                await this.fetchGames();
                this.renderOverview();
                this.renderLibrary();
                this.toast(`SUCCESS: ${data.applied_count} TITLES LINKED & READY`);
            }
        } catch (e) {
            console.error("Apply error:", e);
        }
    }

    /* ==========================================================================
       STEAM INTEGRATION & ACHIEVEMENTS ("SUCCÈS")
       ========================================================================== */

    renderSteamProfileHeader() {
        if (!this.steamProfile) return;
        const p = this.steamProfile;

        const hAvatar = document.getElementById("headerAvatar");
        if (hAvatar && p.avatar_url) hAvatar.src = p.avatar_url;

        const hClan = document.getElementById("headerClanTag");
        if (hClan) hClan.innerText = p.clan_tag || "[141]";

        const hPersona = document.getElementById("headerPersona");
        if (hPersona) hPersona.innerText = p.persona_name || "GHOST_ACTUAL";

        const sAvatar = document.getElementById("steamAvatar");
        if (sAvatar && p.avatar_url) sAvatar.src = p.avatar_url;

        const sClan = document.getElementById("steamClan");
        if (sClan) sClan.innerText = p.clan_tag || "[141]";

        const sPersona = document.getElementById("steamPersona");
        if (sPersona) sPersona.innerText = p.persona_name || "GHOST_ACTUAL_141";

        const sPrestige = document.getElementById("steamPrestige");
        if (sPrestige) sPrestige.innerText = p.prestige_level || "PRESTIGE MASTER";

        const sId = document.getElementById("steamIdVal");
        if (sId) sId.innerText = p.steam_id || "76561198141022141";

        const sStatus = document.getElementById("steamStatusPill");
        if (sStatus) sStatus.innerText = p.profile_state || "ONLINE // DEPLOYED";

        const sReal = document.getElementById("steamRealName");
        if (sReal) sReal.innerText = `${p.real_name || "Simon 'Ghost' Riley"} // ${p.auth_method || "Steam Client"}`;

        const sHours = document.getElementById("steamTotalHours");
        if (sHours) sHours.innerText = p.total_cod_playtime_hours ? p.total_cod_playtime_hours.toLocaleString() : "2,420.5";

        const sAch = document.getElementById("steamTotalAchievements");
        if (sAch) sAch.innerText = p.achievements_unlocked_total || "482";
    }

    async syncSteam() {
        this.playClick();
        const idInput = document.getElementById("steamIdInput");
        const keyInput = document.getElementById("steamApiKeyInput");

        const steamId = idInput ? idInput.value.trim() : "";
        const apiKey = keyInput ? keyInput.value.trim() : "";

        this.toast("INITIATING STEAM SYNCHRONIZATION...");

        try {
            const res = await fetch("/api/steam/sync", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ steam_id: steamId, api_key: apiKey })
            });

            if (res.ok) {
                const data = await res.json();
                this.steamProfile = data.profile;
                this.renderSteamProfileHeader();
                await this.fetchGames();
                this.renderAchievementsShowcase();
                this.toast("STEAM SYNCHRONIZATION COMPLETED // STATS UPDATED");
            }
        } catch (e) {
            console.error("Steam sync error:", e);
        }
    }

    loadGhostProfile() {
        this.playClick();
        const idInput = document.getElementById("steamIdInput");
        if (idInput) idInput.value = "76561198141022141";
        this.syncSteam();
    }

    renderAchievementsShowcase() {
        const selector = document.getElementById("achievementsGameSelector");
        if (!selector) return;

        // Render game selector pills
        selector.innerHTML = this.games.map(g => `
            <button class="filter-pill ${g.id === this.selectedAchGameId ? 'active' : ''}" onclick="app.selectAchievementGame('${g.id}')">
                ${g.title.split(':')[1] ? g.title.split(':')[1].trim() : g.title}
            </button>
        `).join("");

        this.renderAchievementCards();
    }

    selectAchievementGame(gameId) {
        this.playClick();
        this.selectedAchGameId = gameId;
        this.renderAchievementsShowcase();
    }

    renderAchievementCards() {
        const grid = document.getElementById("achievementsListGrid");
        if (!grid) return;

        const game = this.games.find(g => g.id === this.selectedAchGameId);
        if (!game || !game.achievements || game.achievements.length === 0) {
            grid.innerHTML = `
                <div style="grid-column: 1/-1; padding: 20px; color: var(--text-muted); font-family: var(--font-mono);">
                    NO ACHIEVEMENTS RECORDED FOR THIS CLASSIC TITLE.
                </div>
            `;
            return;
        }

        const icons = {
            shield: "🛡️",
            skull: "💀",
            target: "🎯",
            medal: "🎖️",
            star: "⭐",
            hazard: "☢️",
            trophy: "🏆",
            truck: "🚛"
        };

        grid.innerHTML = game.achievements.map(a => `
            <div class="ach-item ${a.unlocked ? 'unlocked' : 'locked'}">
                <span class="ach-icon">${icons[a.icon] || '🎖️'}</span>
                <div class="ach-info">
                    <h4>${a.name} ${a.unlocked ? '<span style="color: var(--accent); font-size: 11px;">[UNLOCKED]</span>' : '<span style="color: #6b7280; font-size: 11px;">[LOCKED]</span>'}</h4>
                    <p>${a.desc}</p>
                </div>
            </div>
        `).join("");
    }

    /* ==========================================================================
       GAME DOSSIER MODAL
       ========================================================================== */

    openDossier(gameId) {
        this.playClick();
        const game = this.games.find(g => g.id === gameId);
        if (!game) return;

        this.currentModalGame = game;

        // Banner
        const hero = document.getElementById("modalHeroBanner");
        if (hero) hero.style.backgroundImage = `url('/assets/banners/${game.id}.jpg')`;

        // Text
        const title = document.getElementById("modalTitle");
        if (title) title.innerText = game.title;

        const sub = document.getElementById("modalSub");
        if (sub) sub.innerText = game.subtitle;

        const series = document.getElementById("modalSeries");
        if (series) series.innerText = game.series.toUpperCase();

        const year = document.getElementById("modalYear");
        if (year) year.innerText = game.release_year;

        const status = document.getElementById("modalStatus");
        if (status) {
            status.innerText = game.is_installed ? "INSTALLED // READY" : "AVAILABLE TO INSTALL";
            status.style.color = game.is_installed ? "var(--accent)" : "var(--accent-sand)";
        }

        const synopsis = document.getElementById("modalSynopsis");
        if (synopsis) synopsis.innerText = game.synopsis;

        // Modes
        const modesList = document.getElementById("modalModesList");
        if (modesList) {
            modesList.innerHTML = (game.modes || []).map(m => `<span class="mode-badge">${m.toUpperCase()}</span>`).join("");
        }

        // Intel
        const dev = document.getElementById("modalDeveloper");
        if (dev) dev.innerText = game.developer;

        const pub = document.getElementById("modalPublisher");
        if (pub) pub.innerText = game.publisher;

        const eng = document.getElementById("modalEngine");
        if (eng) eng.innerText = game.engine;

        const stg = document.getElementById("modalStorage");
        if (stg) stg.innerText = `${game.storage_gb} GB`;

        // Cover
        const cover = document.getElementById("modalCoverImg");
        if (cover) cover.src = `/assets/covers/${game.id}.jpg`;

        // Favorite button text
        const favBtn = document.getElementById("modalFavBtn");
        if (favBtn) favBtn.innerText = game.is_favorite ? "★ FAVORITED" : "☆ FAVORITE";

        // Deploy button text
        const depBtn = document.getElementById("modalDeployBtnText");
        if (depBtn) depBtn.innerText = game.is_installed ? "DEPLOY // LAUNCH" : "DEPLOY PROTOCOL";

        // Achievements tab
        this.renderModalAchievements(game);

        // Specs tab
        this.renderModalSpecs(game);

        // Config tab
        const exeInput = document.getElementById("modalExePath");
        if (exeInput) exeInput.value = game.installed_path || "";

        const argsInput = document.getElementById("modalLaunchArgs");
        if (argsInput) argsInput.value = game.launch_args || "";

        const toggleBtn = document.getElementById("modalToggleInstallBtn");
        if (toggleBtn) toggleBtn.innerText = game.is_installed ? "MARK AS UNINSTALLED" : "MARK AS INSTALLED";

        // Open modal
        this.setDossierTab("briefing");
        const modal = document.getElementById("dossierModal");
        if (modal) modal.classList.add("open");
    }

    closeDossier() {
        this.playClick();
        const modal = document.getElementById("dossierModal");
        if (modal) modal.classList.remove("open");
        this.currentModalGame = null;
    }

    setDossierTab(tabId) {
        this.playClick();
        document.querySelectorAll(".dossier-tab-btn").forEach(btn => {
            btn.classList.toggle("active", btn.dataset.dtab === tabId);
        });
        document.querySelectorAll(".dossier-subtab").forEach(sub => {
            sub.classList.toggle("active", sub.id === `dtab-${tabId}`);
        });
    }

    renderModalAchievements(game) {
        const ach = game.achievements || [];
        const unlocked = ach.filter(a => a.unlocked).length;
        const pct = ach.length ? Math.round((unlocked / ach.length) * 100) : 0;

        const text = document.getElementById("modalAchProgressText");
        if (text) text.innerText = `${unlocked} / ${ach.length} UNLOCKED (${pct}%)`;

        const bar = document.getElementById("modalAchProgressBar");
        if (bar) bar.style.width = `${pct}%`;

        const grid = document.getElementById("modalAchievementsGrid");
        if (!grid) return;

        const icons = { shield: "🛡️", skull: "💀", target: "🎯", medal: "🎖️", star: "⭐", hazard: "☢️", trophy: "🏆", truck: "🚛" };

        grid.innerHTML = ach.map(a => `
            <div class="ach-item ${a.unlocked ? 'unlocked' : 'locked'}">
                <span class="ach-icon">${icons[a.icon] || '🎖️'}</span>
                <div class="ach-info">
                    <h4>${a.name}</h4>
                    <p>${a.desc}</p>
                </div>
            </div>
        `).join("");
    }

    renderModalSpecs(game) {
        const specs = game.specs || {};
        const minEl = document.getElementById("modalMinSpecs");
        const recEl = document.getElementById("modalRecSpecs");

        if (minEl) {
            minEl.innerHTML = `
                <li><strong>OS:</strong> ${specs.min_os || "Windows 10 64-bit"}</li>
                <li><strong>CPU:</strong> ${specs.min_cpu || "Intel Core i3 / AMD Ryzen 3"}</li>
                <li><strong>RAM:</strong> ${specs.min_ram || "8 GB"}</li>
                <li><strong>GPU:</strong> ${specs.min_gpu || "NVIDIA GTX 960 / AMD RX 470"}</li>
            `;
        }

        if (recEl) {
            recEl.innerHTML = `
                <li><strong>OS:</strong> ${specs.rec_os || "Windows 11 64-bit"}</li>
                <li><strong>CPU:</strong> ${specs.rec_cpu || "Intel Core i7 / AMD Ryzen 7"}</li>
                <li><strong>RAM:</strong> ${specs.rec_ram || "16 GB"}</li>
                <li><strong>GPU:</strong> ${specs.rec_gpu || "NVIDIA RTX 3060 / AMD RX 6600"}</li>
            `;
        }
    }

    async saveCustomPath() {
        this.playClick();
        if (!this.currentModalGame) return;

        const input = document.getElementById("modalExePath");
        const path = input ? input.value.trim() : "";

        try {
            const res = await fetch(`/api/games/${this.currentModalGame.id}/update`, {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ installed_path: path, is_installed: Boolean(path) })
            });

            if (res.ok) {
                await this.fetchGames();
                this.toast("EXECUTABLE PATH UPDATED SUCCESSFULLY");
            }
        } catch (e) {
            console.error("Path save error:", e);
        }
    }

    async saveCustomArgs() {
        this.playClick();
        if (!this.currentModalGame) return;

        const input = document.getElementById("modalLaunchArgs");
        const args = input ? input.value.trim() : "";

        try {
            const res = await fetch(`/api/games/${this.currentModalGame.id}/update`, {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ launch_args: args })
            });

            if (res.ok) {
                await this.fetchGames();
                this.toast("CUSTOM LAUNCH ARGUMENTS SAVED");
            }
        } catch (e) {
            console.error("Args save error:", e);
        }
    }

    async markAsInstalledToggle() {
        this.playClick();
        if (!this.currentModalGame) return;

        const nextState = !this.currentModalGame.is_installed;
        try {
            const res = await fetch(`/api/games/${this.currentModalGame.id}/update`, {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ is_installed: nextState })
            });

            if (res.ok) {
                await this.fetchGames();
                this.openDossier(this.currentModalGame.id);
                this.toast(`STATUS UPDATED: ${nextState ? 'INSTALLED' : 'UNINSTALLED'}`);
            }
        } catch (e) {
            console.error("Status toggle error:", e);
        }
    }

    async toggleModalFavorite() {
        this.playClick();
        if (!this.currentModalGame) return;

        const nextFav = !this.currentModalGame.is_favorite;
        try {
            const res = await fetch(`/api/games/${this.currentModalGame.id}/update`, {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ is_favorite: nextFav })
            });

            if (res.ok) {
                await this.fetchGames();
                const favBtn = document.getElementById("modalFavBtn");
                if (favBtn) favBtn.innerText = nextFav ? "★ FAVORITED" : "☆ FAVORITE";
                this.toast(`FAVORITE: ${nextFav ? 'ADDED' : 'REMOVED'}`);
            }
        } catch (e) {
            console.error("Fav toggle error:", e);
        }
    }

    async promptChangeCover() {
        this.playClick();
        const url = prompt("Enter image URL for custom box art cover (or leave empty to reset to tactical military artwork):");
        if (url === null) return;

        if (!this.currentModalGame) return;

        try {
            const res = await fetch(`/api/games/${this.currentModalGame.id}/cover`, {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ image_url: url.trim() })
            });

            if (res.ok) {
                const cover = document.getElementById("modalCoverImg");
                if (cover) cover.src = `/assets/covers/${this.currentModalGame.id}.jpg?t=${Date.now()}`;
                this.renderLibrary();
                this.toast("COVER ART UPDATED SUCCESSFULLY");
            }
        } catch (e) {
            console.error("Cover change error:", e);
        }
    }

    async openModalGameFolder() {
        this.playClick();
        if (!this.currentModalGame) return;

        try {
            const res = await fetch(`/api/games/${this.currentModalGame.id}/folder`, { method: "POST" });
            if (res.ok) {
                const data = await res.json();
                this.toast(data.message || "OPENING GAME FOLDER");
            }
        } catch (e) {
            console.error("Folder open error:", e);
        }
    }

    verifySteamFiles() {
        this.playClick();
        if (!this.currentModalGame || !this.currentModalGame.steam_appid) {
            this.toast("TITLE IS NOT LINKED VIA STEAM CLIENT.");
            return;
        }
        window.open(`steam://validate/${this.currentModalGame.steam_appid}`, "_blank");
        this.toast(`ISSUED FILE VERIFY TO STEAM: [steam://validate/${this.currentModalGame.steam_appid}]`);
    }

    /* ==========================================================================
       GAME LAUNCHING
       ========================================================================== */

    launchFeaturedGame(mode = "default") {
        this.launchGame(this.featuredGameId, mode);
    }

    launchCurrentModalGame(mode = "default") {
        if (!this.currentModalGame) return;
        this.launchGame(this.currentModalGame.id, mode);
    }

    async launchGame(gameId, mode = "default") {
        this.playDeploy();
        const game = this.games.find(g => g.id === gameId);
        const title = game ? game.title : "Call of Duty";

        this.toast(`DEPLOYING: ${title.toUpperCase()} [${mode.toUpperCase()}]`);

        try {
            const res = await fetch(`/api/games/${gameId}/launch`, {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ mode: mode })
            });

            if (res.ok) {
                const data = await res.json();
                this.toast(`${data.message || 'COMMAND ISSUED'}`);
            } else {
                this.toast(`DEPLOYMENT DISPATCHED: ${title}`);
            }
        } catch (e) {
            this.toast(`DEPLOYMENT DISPATCHED: ${title}`);
        }
    }

    /* ==========================================================================
       NOTIFICATIONS & TOASTS
       ========================================================================== */

    toast(message) {
        const container = document.getElementById("toastContainer");
        if (!container) return;

        const toast = document.createElement("div");
        toast.className = "toast";
        toast.innerText = message;

        container.appendChild(toast);

        setTimeout(() => {
            toast.style.opacity = "0";
            toast.style.transform = "translateX(30px)";
            toast.style.transition = "all 0.3s ease";
            setTimeout(() => toast.remove(), 300);
        }, 3500);
    }
}

// Global App Instance
let app;
window.addEventListener("DOMContentLoaded", () => {
    app = new CodHQApp();
});
