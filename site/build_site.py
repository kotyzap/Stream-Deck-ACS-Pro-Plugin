#!/usr/bin/env python3
"""Generates docs/index.html (GitHub Pages) for Deck for AXIS Camera Station Pro & 5.
Pavel Kotyza <kotyza@gmail.com> — https://www.4xs.dev
"""
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
REPO = "https://github.com/kotyzap/Stream-Deck-ACS-Pro-Plugin"
DL = f"{REPO}/raw/main/dist/com.4xsdev.acs-pro-kofi.streamDeckPlugin"
ACS_DOCS = "https://help.axis.com/en-us/axis-camera-station-pro#hotkeys"

FONTS = '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;700&family=IBM+Plex+Sans:wght@400;500&family=IBM+Plex+Mono:wght@400&display=swap">'

CSS = """
:root{--bg:#f7f5f1;--bg2:#efece6;--fg:#1c1b19;--fg2:#5f5c56;--line:#e0dcd4;--card:#ffffff;--accent:#b0800a;--accent-fg:#ffffff;--deck:#1c1c1e}
[data-theme=dark]{--bg:#161615;--bg2:#1f1f1e;--fg:#f2f0ec;--fg2:#a09c94;--line:#2c2b29;--card:#1d1d1c;--accent:#ffcc33;--accent-fg:#161615}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--fg);font-family:"IBM Plex Sans",system-ui,-apple-system,sans-serif;font-size:17px;line-height:1.55;-webkit-font-smoothing:antialiased}
a{color:var(--accent);text-decoration:none}a:hover{color:var(--fg)}
h1,h2,h3{font-family:"Space Grotesk","Helvetica Neue",Arial,sans-serif;letter-spacing:-0.02em;margin:0}
code,kbd{font-family:"IBM Plex Mono",ui-monospace,Menlo,monospace;font-size:0.9em}
kbd{background:var(--bg2);border:1px solid var(--line);border-radius:6px;padding:1px 7px}
.wrap{max-width:1040px;margin:0 auto;padding:0 28px}
nav{display:flex;align-items:center;justify-content:space-between;height:68px}
.brand{display:flex;align-items:center;gap:12px;font-family:"Space Grotesk",sans-serif;font-weight:700;font-size:18px;color:var(--fg)}
.mark{width:30px;height:30px;border-radius:8px;background:#ffcc33;color:#1c1c1e;display:grid;place-items:center}
.navlinks{display:flex;align-items:center;gap:22px;font-size:15px;color:var(--fg2)}
.navlinks a{color:var(--fg2)}.navlinks a:hover{color:var(--fg)}
.toggle{width:40px;height:26px;border-radius:13px;border:1px solid var(--line);background:var(--bg2);position:relative;cursor:pointer;padding:0}
.toggle::after{content:"";position:absolute;top:3px;left:3px;width:18px;height:18px;border-radius:50%;background:var(--fg);transition:left .15s}
[data-theme=dark] .toggle::after{left:17px}
.hero{display:grid;grid-template-columns:minmax(0,4fr) minmax(0,7fr);gap:40px;align-items:center;padding:48px 0 56px}
.hero h1{font-size:44px;line-height:1.05;font-weight:700}
.hero p{font-size:19px;color:var(--fg2);margin:20px 0 28px}
.cta{display:flex;gap:10px;align-items:center;flex-wrap:wrap}
.btn{display:inline-flex;align-items:center;gap:8px;background:var(--accent);color:var(--accent-fg);font-weight:500;padding:12px 16px;border-radius:10px;font-size:15px}
.btn:hover{color:var(--accent-fg);filter:brightness(1.08)}
.btn.ghost{background:transparent;color:var(--fg);border:1px solid var(--line)}
.meta{font-size:14px;color:var(--fg2)}
.hero img{width:100%;height:auto;display:block}
section{padding:56px 0;border-top:1px solid var(--line)}
.eyebrow{font-family:"IBM Plex Mono",monospace;font-size:13px;letter-spacing:.08em;text-transform:uppercase;color:var(--accent);margin-bottom:12px}
h2{font-size:32px;font-weight:700;margin-bottom:12px}
.lead{font-size:18px;color:var(--fg2);max-width:640px;margin:0 0 32px}
.grid3{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:20px}
.card{background:var(--card);border:1px solid var(--line);border-radius:14px;padding:22px}
.card h3{font-size:18px;margin-bottom:8px}
.card p{margin:0;color:var(--fg2);font-size:15.5px}
.num{font-family:"IBM Plex Mono",monospace;color:var(--accent);font-size:13px;margin-bottom:10px}
.sheet{background:var(--deck);border-radius:16px;padding:20px;margin:0 0 28px}
.sheet img{display:block;width:100%;max-width:760px;margin:0 auto;height:auto}
table{width:100%;border-collapse:collapse;font-size:15.5px}
td{padding:10px 0;border-top:1px solid var(--line);vertical-align:top}
td:first-child{font-weight:500;white-space:nowrap;padding-right:22px}
td:last-child{color:var(--fg2)}
.decks{display:grid;grid-template-columns:minmax(0,3fr) minmax(0,8fr);gap:24px;align-items:end}.decks img{width:100%;height:auto;display:block;border-radius:12px}
.flow{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:12px;align-items:stretch}
footer{padding:36px 0 48px;border-top:1px solid var(--line);display:flex;justify-content:space-between;gap:20px;flex-wrap:wrap;font-size:14px;color:var(--fg2)}
footer a{color:var(--fg2)}footer a:hover{color:var(--fg)}
@media (max-width:820px){.decks{grid-template-columns:1fr}.hero{grid-template-columns:1fr;padding-top:24px}.hero h1{font-size:38px}.grid3,.flow{grid-template-columns:1fr}.navlinks span{display:none}}

.cardlink{display:block;text-decoration:none;color:inherit;transition:border-color .15s}
.cardlink:hover{border-color:var(--accent)}
.cardlink h3{color:var(--fg)}
"""

GH_ICON = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M9 19c-4.3 1.4-4.3-2.5-6-3m12 5v-3.5c0-1 .1-1.4-.5-2 2.8-.3 5.5-1.4 5.5-6a4.6 4.6 0 0 0-1.3-3.2 4.2 4.2 0 0 0-.1-3.2s-1.1-.3-3.5 1.3a12.3 12.3 0 0 0-6.2 0C6.5 2.8 5.4 3.1 5.4 3.1a4.2 4.2 0 0 0-.1 3.2A4.6 4.6 0 0 0 4 9.5c0 4.6 2.7 5.7 5.5 6-.6.6-.6 1.2-.5 2V21"/></svg>'
DL_ICON = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 3v12m0 0 4-4m-4 4-4-4M4 17v2a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2v-2"/></svg>'
MARK = '<svg width="18" height="18" viewBox="0 0 24 24" fill="#1c1c1e" aria-hidden="true"><rect x="2" y="7" width="12" height="10" rx="2"/><path d="M14 10l7-4v12l-7-4z"/></svg>'

BODY = f"""
<div class="wrap">
  <nav>
    <a class="brand" href="#"><span class="mark">{MARK}</span><span>Deck for AXIS Camera Station Pro &amp; 5</span></a>
    <div class="navlinks"><a href="#hotkeys">Hotkeys</a><a href="#actions">Actions</a><a href="#decks">Decks</a><a href="#install">Install</a><a href="{REPO}">{GH_ICON}</a><button class="toggle" id="theme" aria-label="Toggle dark mode" onclick="toggleTheme()"></button></div>
  </nav>

  <div class="hero">
    <div>
      <h1>ACS 5 and ACS Pro on physical keys.</h1>
      <p>Play, previous / next recording, bookmark, live / recordings, next camera, PTZ presets — and every camera or view you map in AXIS Camera Station. For the AXIS Camera Station 5 and AXIS Camera Station Pro client — same hotkeys, one plugin. Windows natively; on a Mac through Parallels, VMware or Remote Desktop.</p>
      <div class="cta">
        <a class="btn" href="{DL}">{DL_ICON}Download plugin</a>
        <a class="btn ghost" href="{REPO}">Source on GitHub</a>
      </div>
      <p class="meta" style="margin-top:16px">Windows 10+ · macOS 12+ · Stream Deck 6.9+ · one-click install with a ready profile for Mini, MK.2 and XL. Free and open source (MIT). Also on the Elgato Marketplace; this GitHub build adds a <a href="https://ko-fi.com/K3K6RR4LY">Buy me a Ko-fi</a> key.</p>
    </div>
    <img src="img/hero-decks.png" width="1600" height="1434" alt="The three bundled profiles on Stream Deck XL, MK.2 and Mini: playback, navigation, PTZ presets and camera hotkeys for ACS Pro">
  </div>

  <section id="hotkeys">
    <div class="eyebrow">Read this first</div>
    <h2>ACS runs on hotkeys you control.</h2>
    <p class="lead">AXIS Camera Station — 5 and Pro alike — is driven by keyboard hotkeys — <kbd>F2</kbd> opens the Hotkeys tab where every action gets <kbd>Ctrl</kbd> + a key or <kbd>F2</kbd>–<kbd>F12</kbd>. Axis documents only a few defaults, and "navigate to camera / view" has none. The plugin embraces that:</p>
    <div class="grid3">
      <div class="card"><div class="num">✓ documented</div><h3>Sent as Axis defines them</h3><p>Zoom <kbd>Ctrl</kbd> <kbd>+</kbd> / <kbd>−</kbd>, Help <kbd>F1</kbd>, Hotkeys <kbd>F2</kbd>, Logs <kbd>F4</kbd>, Configuration <kbd>F5</kbd>, Auto focus <kbd>F10</kbd>, Exit full screen <kbd>Esc</kbd>.</p></div>
      <div class="card"><div class="num">suggested</div><h3>Mirror once in ACS, or edit the key</h3><p>Play/Pause <kbd>Ctrl</kbd> <kbd>Space</kbd>, Next recording <kbd>Ctrl</kbd> <kbd>L</kbd>, Bookmark <kbd>Ctrl</kbd> <kbd>B</kbd>… In ACS press F2, click the action's keyboard field, press the same combo. Or type your own combo into the key's Hotkey field.</p></div>
      <div class="card"><div class="num">yours</div><h3>Cameras, views, sequences</h3><p>Map <kbd>Ctrl</kbd> <kbd>5</kbd> to "Navigate to camera: Lobby" in ACS, make an <strong>ACS Hotkey</strong> key "Lobby → Ctrl+5". A Stream Deck XL becomes a camera wall selector.</p></div>
    </div>
    <p class="meta" style="margin-top:20px">Every key shows the combo it sends in small print. Rules from Axis's <a href="{ACS_DOCS}">Hotkeys</a> chapter of the ACS Pro user manual.</p>
  </section>

  <section id="actions">
    <div class="eyebrow">Three actions</div>
    <h2>29 commands, a free hotkey, and Activate.</h2>
    <p class="lead">The plugin adds a "Deck for AXIS Camera Station Pro &amp; 5" group to the Stream Deck action list.</p>
    <div class="sheet"><img src="img/actions.png" width="1220" height="620" alt="All key arts: playback, bookmark, export marker, live/recordings, camera / tab / cell navigation, open views, exit full screen, presets 1–4, zoom, focus, auto focus, hotkeys, logs, configuration, help, custom hotkeys, activate"></div>
    <table>
      <tr><td>ACS Command · Recordings</td><td>Play / pause · previous / next recording · frame step back / forward · add bookmark · export marker · switch live / recordings.</td></tr>
      <tr><td>ACS Command · Navigation</td><td>Next / previous camera or view · next / previous tab · next / previous cell in split view · open views · exit full screen.</td></tr>
      <tr><td>ACS Command · PTZ</td><td>Go to preset 1–4 · zoom in / out · focus farther / nearer · auto focus.</td></tr>
      <tr><td>ACS Command · System</td><td>Hotkeys <kbd>F2</kbd> · Logs <kbd>F4</kbd> · Configuration <kbd>F5</kbd> · Help <kbd>F1</kbd>.</td></tr>
      <tr><td>ACS Hotkey</td><td>Any combo, your title, a colour — for everything you map yourself in ACS.</td></tr>
      <tr><td>Activate ACS</td><td>Brings ACS to the front so the next hotkey lands in it — the client window on Windows, the hosting app (Parallels, VMware, Windows App) on a Mac. Chain it first in a Multi Action.</td></tr>
    </table>
    <p class="meta" style="margin-top:20px">Combo format <code>Ctrl+Shift+F5</code>: Ctrl / Alt / Shift; A–Z, 0–9, F1–F12, Space, Tab, Esc, Enter, arrows, Plus, Minus and more.</p>
  </section>

  <section id="decks">
    <div class="eyebrow">Every deck size</div>
    <h2>Mini, MK.2, XL — a profile for each.</h2>
    <p class="lead">The installer carries three ready-made profiles — <strong>ACS Pro</strong> (MK.2, 5×3), <strong>ACS Pro Mini</strong> (3×2) and <strong>ACS Pro XL</strong> (8×4) — and Stream Deck installs only the one that matches your device. The XL's bottom row has four camera / view hotkey examples to rename.</p>
    <div class="decks"><img src="img/deck-mini.png" width="568" height="408" alt="Stream Deck Mini profile: previous, play, next, bookmark, live/recordings, next camera"><img src="img/deck-xl.png" width="1368" height="728" alt="Stream Deck XL profile: playback row, PTZ row, navigation row, camera hotkeys and system keys"></div>
  </section>

  <section id="install">
    <div class="eyebrow">Install</div>
    <h2>Three steps, once.</h2>
    <div class="grid3">
      <div class="card"><div class="num">1</div><h3>Download and double-click</h3><p><code>com.4xsdev.acs-pro.streamDeckPlugin</code> — Stream Deck asks to install the plugin. It brings the actions and a ready profile for your deck (Mini, MK.2 or XL).</p></div>
      <div class="card"><div class="num">2</div><h3>Mirror the combos in ACS</h3><p>In the ACS client press <kbd>F2</kbd>. For each key you use, click the action's keyboard field and press the combo shown on the key — or edit the key to match what ACS already has.</p></div>
      <div class="card"><div class="num">3</div><h3>Press Activate, then play</h3><p>Hotkeys go to the front window. Press <strong>Activate ACS</strong> (or click into ACS) and the rest of the deck is live.</p></div>
    </div>
    <p class="meta" style="margin-top:24px">Limits: the ACS client is a Windows application — on a Mac it runs in Parallels / VMware / Remote Desktop and the plugin sends the combos there (⌃ arrives as Ctrl); the plugin cannot tell whether ACS is focused. Written to Axis's documented hotkey rules but not yet tested against a running ACS client — reports welcome via <a href="{REPO}/issues">GitHub issues</a>.</p>
  </section>


  <section id="more">
    <div class="eyebrow">More from 4xs.dev</div>
    <h2>Other Stream Deck plugins.</h2>
    <p class="lead">Physical keys for the tools you already use. All free and open source.</p>
    <div class="grid3">
      <a class="card cardlink" href="https://kotyzap.github.io/Stream-Deck-Claude-Plugin/"><h3>Deck for Claude ↗</h3><p>Answer permission prompts, replies, shortcuts & status for the Claude desktop app</p></a>
      <a class="card cardlink" href="https://kotyzap.github.io/Stream-Deck-Axis-Cam-CamStreamer-Plugin/"><h3>Camera Deck for Axis &amp; CamStreamer ↗</h3><p>PTZ, presets, overlays and CamStreamer/CamSwitcher control for Axis cameras</p></a>
      <a class="card cardlink" href="https://kotyzap.github.io/Stream-Deck-ACS-Edge-Plugin/"><h3>Deck for AXIS Camera Station Edge ↗</h3><p>Recording playback, PTZ and view controls for ACS Edge</p></a>
      <a class="card cardlink" href="https://kotyzap.github.io/Stream-Deck-Genetec-Plugin/"><h3>Deck for Genetec Security Desk ↗</h3><p>Playback, alarms, tiles, PTZ, doors and any camera by logical ID for Security Desk</p></a>
    </div>
  </section>

  <footer>
    <div>Pavel Kotyza · <a href="https://www.4xs.dev">4xs.dev</a> · MIT License · <a href="https://ko-fi.com/K3K6RR4LY">Buy me a Ko-fi</a></div>
    <div>Independent project; not affiliated with Axis Communications or Elgato. AXIS is a trademark of Axis AB.</div>
  </footer>
</div>
"""

JS = """
<script>
(function(){var t=null;try{t=localStorage.getItem('theme')}catch(e){}
if(!t&&window.matchMedia&&window.matchMedia('(prefers-color-scheme: dark)').matches)t='dark';
if(t==='dark')document.documentElement.setAttribute('data-theme','dark');})();
function toggleTheme(){var r=document.documentElement,d=r.getAttribute('data-theme')==='dark';
if(d)r.removeAttribute('data-theme');else r.setAttribute('data-theme','dark');
try{localStorage.setItem('theme',d?'light':'dark')}catch(e){}}
</script>"""


def write_index():
    html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Deck for AXIS Camera Station Pro &amp; 5</title>
<meta name="description" content="Stream Deck plugin for the AXIS Camera Station Pro and ACS 5 Windows client: playback, bookmarks, camera navigation, PTZ presets and any ACS hotkey on physical keys. Profiles for Mini, MK.2 and XL.">
{FONTS}
<style>{CSS}</style>
</head>
<body>
{BODY}
{JS}
</body>
</html>
"""
    (ROOT / "docs" / "index.html").write_text(html)


if __name__ == "__main__":
    write_index()
    print("ok")
