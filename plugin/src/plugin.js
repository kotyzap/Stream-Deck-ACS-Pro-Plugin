// Deck for AXIS Camera Station Pro & 5 — Stream Deck plugin
// Pavel Kotyza <kotyza@gmail.com> — https://www.4xs.dev
//
// The ACS Pro / ACS 5 client is a Windows application driven by keyboard hotkeys (F2 → Hotkeys tab).
// A keyboard hotkey there is Ctrl + key or F2–F12; every action can be re-mapped by the user. Only a few
// combos are documented by Axis; the rest below are suggestions the user mirrors in ACS once, or overrides per key.
import streamDeck, { SingletonAction } from "@elgato/streamdeck";
import { execFile } from "node:child_process";
import { platform } from "node:os";

const PLUGIN = "com.4xsdev.acs-pro";
const AMBER = "#ffcc33", BLUE = "#4da3ff", GREEN = "#34c759", GREY = "#9a9a9e";

// ---------------------------------------------------------------- commands
// hotkey: human form ("Ctrl+Shift+F5"); doc: true = documented by Axis, false = suggested (assign in ACS Hotkeys).
const CMD = {
    // Recordings
    "play":        { title: "Play /\nPause",    color: AMBER, glyph: "play",     hotkey: "Ctrl+Space",       doc: false },
    "prev":        { title: "Prev\nrecording",  color: AMBER, glyph: "prev",     hotkey: "Ctrl+J",           doc: false },
    "next":        { title: "Next\nrecording",  color: AMBER, glyph: "next",     hotkey: "Ctrl+L",           doc: false },
    "step-back":   { title: "Frame\nback",      color: AMBER, glyph: "back",     hotkey: "Ctrl+Left",        doc: false },
    "step-fwd":    { title: "Frame\nforward",   color: AMBER, glyph: "fwd",      hotkey: "Ctrl+Right",       doc: false },
    "bookmark":    { title: "Add\nbookmark",    color: AMBER, glyph: "flag",     hotkey: "Ctrl+B",           doc: false },
    "marker":      { title: "Export\nmarker",   color: AMBER, glyph: "marker",   hotkey: "Ctrl+E",           doc: false },
    "live-rec":    { title: "Live /\nRecordings", color: AMBER, glyph: "liverec", hotkey: "Ctrl+R",          doc: false },
    // Navigation
    "next-cam":    { title: "Next\ncamera",     color: BLUE,  glyph: "camnext",  hotkey: "Ctrl+N",           doc: false },
    "prev-cam":    { title: "Prev\ncamera",     color: BLUE,  glyph: "camprev",  hotkey: "Ctrl+Shift+N",     doc: false },
    "next-tab":    { title: "Next\ntab",        color: BLUE,  glyph: "tabnext",  hotkey: "Ctrl+Tab",         doc: false },
    "prev-tab":    { title: "Prev\ntab",        color: BLUE,  glyph: "tabprev",  hotkey: "Ctrl+Shift+Tab",   doc: false },
    "next-cell":   { title: "Next\ncell",       color: BLUE,  glyph: "cellnext", hotkey: "Ctrl+]",           doc: false },
    "prev-cell":   { title: "Prev\ncell",       color: BLUE,  glyph: "cellprev", hotkey: "Ctrl+[",           doc: false },
    "views":       { title: "Open\nviews",      color: BLUE,  glyph: "grid",     hotkey: "Ctrl+Shift+V",     doc: false },
    "fullscreen-exit": { title: "Exit\nfull screen", color: BLUE, glyph: "shrink", hotkey: "Esc",           doc: true },
    // PTZ
    "preset-1":    { title: "Preset 1",         color: GREEN, glyph: "p1",       hotkey: "Ctrl+1",           doc: false },
    "preset-2":    { title: "Preset 2",         color: GREEN, glyph: "p2",       hotkey: "Ctrl+2",           doc: false },
    "preset-3":    { title: "Preset 3",         color: GREEN, glyph: "p3",       hotkey: "Ctrl+3",           doc: false },
    "preset-4":    { title: "Preset 4",         color: GREEN, glyph: "p4",       hotkey: "Ctrl+4",           doc: false },
    "zoom-in":     { title: "Zoom in",          color: GREEN, glyph: "zoomin",   hotkey: "Ctrl+Plus",        doc: true },
    "zoom-out":    { title: "Zoom out",         color: GREEN, glyph: "zoomout",  hotkey: "Ctrl+Minus",       doc: true },
    "focus-far":   { title: "Focus\nfarther",   color: GREEN, glyph: "focusfar", hotkey: "Ctrl+Shift+Plus",  doc: false },
    "focus-near":  { title: "Focus\nnearer",    color: GREEN, glyph: "focusnear", hotkey: "Ctrl+Shift+Minus", doc: false },
    "autofocus":   { title: "Auto\nfocus",      color: GREEN, glyph: "af",       hotkey: "F10",              doc: true },
    // System
    "hotkeys":     { title: "Hotkeys",          color: GREY,  glyph: "keys",     hotkey: "F2",               doc: true },
    "logs":        { title: "Logs",             color: GREY,  glyph: "log",      hotkey: "F4",               doc: true },
    "config":      { title: "Configuration",    color: GREY,  glyph: "gear",     hotkey: "F5",               doc: true },
    "help":        { title: "Help",             color: GREY,  glyph: "help",     hotkey: "F1",               doc: true },
};
export { CMD };

// ---------------------------------------------------------------- key art
// Glyphs: stroked/filled paths on a 144×144 key, centred around (72,56). "C" is replaced by the key colour.
const S = 'fill="none" stroke="C" stroke-width="9" stroke-linecap="round" stroke-linejoin="round"';
const GLYPH = {
    play:     `<path d="M50 32v48l38-24z" fill="C"/><rect x="94" y="32" width="8" height="48" fill="C" opacity=".55"/>`,
    prev:     `<path d="M92 34v44L58 56z" fill="C"/><rect x="48" y="34" width="8" height="44" fill="C"/>`,
    next:     `<path d="M52 34v44l34-22z" fill="C"/><rect x="88" y="34" width="8" height="44" fill="C"/>`,
    back:     `<path d="M84 34L58 56l26 22" ${S}/>`,
    fwd:      `<path d="M60 34l26 22-26 22" ${S}/>`,
    flag:     `<path d="M52 82V32" ${S}/><path d="M52 34h38l-8 12 8 12H52z" fill="C"/>`,
    marker:   `<path d="M46 80V32M98 80V32" ${S}/><rect x="60" y="46" width="24" height="20" rx="3" fill="C"/>`,
    liverec:  `<circle cx="56" cy="56" r="12" fill="C"/><path d="M78 44h22v24H78z" fill="none" stroke="C" stroke-width="7"/><path d="M84 50l10 6-10 6z" fill="C"/>`,
    camnext:  `<rect x="36" y="44" width="40" height="28" rx="5" fill="C"/><path d="M76 52l14-8v24l-14-8z" fill="C"/><path d="M98 46l10 10-10 10" ${S}/>`,
    camprev:  `<rect x="68" y="44" width="40" height="28" rx="5" fill="C"/><path d="M68 52l-14-8v24l14-8z" fill="C"/><path d="M46 46L36 56l10 10" ${S}/>`,
    tabnext:  `<path d="M40 40h40a6 6 0 0 1 6 6v34H40z" fill="none" stroke="C" stroke-width="7"/><path d="M86 40h18v40H86" fill="none" stroke="C" stroke-width="7" opacity=".5"/><path d="M60 52l10 8-10 8" ${S}/>`,
    tabprev:  `<path d="M104 40H64a6 6 0 0 0-6 6v34h46z" fill="none" stroke="C" stroke-width="7"/><path d="M58 40H40v40h18" fill="none" stroke="C" stroke-width="7" opacity=".5"/><path d="M84 52l-10 8 10 8" ${S}/>`,
    cellnext: `<rect x="40" y="36" width="28" height="18" fill="none" stroke="C" stroke-width="5"/><rect x="76" y="36" width="28" height="18" fill="C"/><rect x="40" y="60" width="28" height="18" fill="none" stroke="C" stroke-width="5"/><rect x="76" y="60" width="28" height="18" fill="none" stroke="C" stroke-width="5"/>`,
    cellprev: `<rect x="40" y="36" width="28" height="18" fill="C"/><rect x="76" y="36" width="28" height="18" fill="none" stroke="C" stroke-width="5"/><rect x="40" y="60" width="28" height="18" fill="none" stroke="C" stroke-width="5"/><rect x="76" y="60" width="28" height="18" fill="none" stroke="C" stroke-width="5"/>`,
    grid:     `<rect x="42" y="34" width="26" height="20" rx="3" fill="C"/><rect x="76" y="34" width="26" height="20" rx="3" fill="C"/><rect x="42" y="60" width="26" height="20" rx="3" fill="C"/><rect x="76" y="60" width="26" height="20" rx="3" fill="C"/>`,
    shrink:   `<path d="M64 48L44 28M64 48V34M64 48H50M80 64l20 20M80 64v14M80 64h14" ${S}/>`,
    zoomin:   `<circle cx="66" cy="52" r="20" fill="none" stroke="C" stroke-width="8"/><path d="M81 67l16 16" stroke="C" stroke-width="9" stroke-linecap="round"/><path d="M66 42v20M56 52h20" stroke="C" stroke-width="7" stroke-linecap="round"/>`,
    zoomout:  `<circle cx="66" cy="52" r="20" fill="none" stroke="C" stroke-width="8"/><path d="M81 67l16 16" stroke="C" stroke-width="9" stroke-linecap="round"/><path d="M56 52h20" stroke="C" stroke-width="7" stroke-linecap="round"/>`,
    focusfar: `<path d="M40 40h-2v-6h10M104 40h2v-6H96M40 72h-2v6h10M104 72h2v6H96" ${S}/><circle cx="72" cy="56" r="8" fill="C"/>`,
    focusnear:`<path d="M40 40h-2v-6h10M104 40h2v-6H96M40 72h-2v6h10M104 72h2v6H96" ${S}/><circle cx="72" cy="56" r="20" fill="none" stroke="C" stroke-width="8"/>`,
    af:       `<path d="M40 40h-2v-6h10M104 40h2v-6H96M40 72h-2v6h10M104 72h2v6H96" ${S}/><text x="72" y="66" font-family="Helvetica, Arial, sans-serif" font-size="30" font-weight="700" fill="C" text-anchor="middle">AF</text>`,
    keys:     `<rect x="34" y="36" width="76" height="40" rx="6" fill="none" stroke="C" stroke-width="7"/><path d="M46 48h6M58 48h6M70 48h6M82 48h6M94 48h6M46 64h52" stroke="C" stroke-width="5" stroke-linecap="round"/>`,
    log:      `<path d="M48 30h34l14 14v40H48z" fill="none" stroke="C" stroke-width="7" stroke-linejoin="round"/><path d="M58 54h28M58 66h28" stroke="C" stroke-width="6" stroke-linecap="round"/>`,
    gear:     `<circle cx="72" cy="56" r="12" fill="none" stroke="C" stroke-width="8"/><path d="M72 28v10M72 74v10M44 56h10M90 56h10M52 36l7 7M85 69l7 7M92 36l-7 7M59 69l-7 7" stroke="C" stroke-width="8" stroke-linecap="round"/>`,
    help:     `<circle cx="72" cy="56" r="24" fill="none" stroke="C" stroke-width="8"/><path d="M63 49a9 9 0 1 1 13 8c-3 2-4 4-4 7" fill="none" stroke="C" stroke-width="7" stroke-linecap="round"/><circle cx="72" cy="70" r="4" fill="C"/>`,
    window:   `<rect x="40" y="36" width="64" height="44" rx="6" fill="none" stroke="C" stroke-width="8"/><path d="M40 48h64" stroke="C" stroke-width="6"/><circle cx="49" cy="42" r="2.5" fill="C"/><circle cx="57" cy="42" r="2.5" fill="C"/>`,
    key:      `<rect x="36" y="38" width="72" height="40" rx="8" fill="none" stroke="C" stroke-width="7"/>`,
};
for (const n of [1, 2, 3, 4]) GLYPH[`p${n}`] = `<path d="M40 40h-2v-6h10M104 40h2v-6H96M40 72h-2v6h10M104 72h2v6H96" ${S}/><text x="72" y="70" font-family="Helvetica, Arial, sans-serif" font-size="40" font-weight="700" fill="C" text-anchor="middle">${n}</text>`;

const esc = (t) => String(t).replace(/&/g, "&amp;").replace(/</g, "&lt;");
/** Key: colour bar, glyph, title (≤2 lines) and the hotkey in small mono at the bottom. `inner` overrides the glyph (Hotkey key). */
function keyImage(glyph, color, title, hotkey, inner) {
    const lines = String(title).split("\n").slice(0, 2);
    const size = Math.max(...lines.map((l) => l.length)) <= 10 ? 18 : 15;
    const y0 = lines.length === 1 ? 108 : 100;
    const text = lines.map((l, i) =>
        `<text x="72" y="${y0 + i * (size + 1)}" font-family="Helvetica, Arial, sans-serif" font-size="${size}" font-weight="700" fill="#f2f2f7" text-anchor="middle">${esc(l)}</text>`).join("");
    const hk = hotkey ? `<text x="72" y="135" font-family="Menlo, Consolas, monospace" font-size="11" fill="#8e8e93" text-anchor="middle">${esc(hotkey)}</text>` : "";
    const art = (inner ?? GLYPH[glyph] ?? "").replace(/"C"/g, `"${color}"`);
    const svg = `<svg xmlns="http://www.w3.org/2000/svg" width="144" height="144" viewBox="0 0 144 144">
  <rect width="144" height="144" rx="18" fill="#1c1c1e"/><rect width="144" height="10" fill="${color}"/>${art}${text}${hk}</svg>`;
    return `data:image/svg+xml;base64,${Buffer.from(svg).toString("base64")}`;
}
/** Hotkey key: rounded key shape with the last key name inside, title + full combo below. */
function hotkeyImage(title, hotkey, colorName) {
    const color = { camera: BLUE, recording: AMBER, ptz: GREEN }[colorName] ?? GREY;
    const label = hotkey ? hotkey.split("+").filter(Boolean).pop() ?? "+" : "?";
    const inner = `<rect x="36" y="34" width="72" height="44" rx="8" fill="none" stroke="C" stroke-width="7"/><text x="72" y="66" font-family="Helvetica, Arial, sans-serif" font-size="${label.length > 3 ? 20 : 28}" font-weight="700" fill="C" text-anchor="middle">${esc(label)}</text>`;
    return keyImage(null, color, title || "Hotkey", hotkey || "set hotkey", inner);
}
const activateImage = () => keyImage("window", GREY, "Activate\nACS", "");
export { GLYPH, keyImage, hotkeyImage, activateImage };

// ---------------------------------------------------------------- hotkeys → SendKeys
// "Ctrl+Shift+F5" → "^+{F5}". Modifiers: Ctrl ^, Alt %, Shift +, Win (unsupported by SendKeys → error).
const NAMED = {
    space: " ", enter: "{ENTER}", return: "{ENTER}", esc: "{ESC}", escape: "{ESC}", tab: "{TAB}", backspace: "{BACKSPACE}",
    delete: "{DELETE}", del: "{DELETE}", insert: "{INSERT}", home: "{HOME}", end: "{END}", pageup: "{PGUP}", pagedown: "{PGDN}",
    up: "{UP}", down: "{DOWN}", left: "{LEFT}", right: "{RIGHT}", plus: "{+}", minus: "-", "+": "{+}", "-": "-",
    "^": "{^}", "%": "{%}", "~": "{~}", "(": "{(}", ")": "{)}", "[": "{[}", "]": "{]}", "{": "{{}", "}": "{}}",
};
export function toSendKeys(hotkey) {
    const parts = String(hotkey).trim().split("+").map((p) => p.trim()).filter(Boolean);
    // "Ctrl++" / "Ctrl+Shift+Plus": a trailing empty part means the key itself was "+"
    if (/\+\s*$/.test(String(hotkey).trim())) parts.push("+");
    if (!parts.length) throw new Error("empty hotkey");
    const key = parts.pop();
    let mods = "";
    for (const m of parts) {
        const l = m.toLowerCase();
        if (l === "ctrl" || l === "control") mods += "^";
        else if (l === "alt") mods += "%";
        else if (l === "shift") mods += "+";
        else throw new Error(`unknown modifier "${m}"`);
    }
    const l = key.toLowerCase();
    let k;
    if (NAMED[l] !== undefined) k = NAMED[l];
    else if (/^f([1-9]|1[0-6])$/.test(l)) k = `{${l.toUpperCase()}}`;
    else if (key.length === 1) k = l;
    else throw new Error(`unknown key "${key}"`);
    return mods + k;
}

function run(cmd, args) {
    return new Promise((resolve, reject) => execFile(cmd, args, (err) => (err ? reject(err) : resolve())));
}
const ps = (script) => run("powershell", ["-NoProfile", "-NonInteractive", "-WindowStyle", "Hidden", "-Command", script]);

async function sendHotkey(hotkey) {
    if (platform() !== "win32") throw new Error("AXIS Camera Station Pro / 5 client runs on Windows only");
    const keys = toSendKeys(hotkey).replace(/'/g, "''");
    await ps(`Add-Type -AssemblyName System.Windows.Forms; [System.Windows.Forms.SendKeys]::SendWait('${keys}')`);
}

async function activateWindow(titlePart) {
    if (platform() !== "win32") throw new Error("Windows only");
    const t = String(titlePart).replace(/'/g, "''");
    // AppActivate matches a window whose title starts with or ends with the string; fall back to the ACS process' main window.
    await ps(`$ok = (New-Object -ComObject WScript.Shell).AppActivate('${t}'); if (-not $ok) { $p = Get-Process | Where-Object { $_.MainWindowTitle -like '*${t}*' } | Select-Object -First 1; if ($p) { (New-Object -ComObject WScript.Shell).AppActivate($p.Id) | Out-Null } else { exit 2 } }`);
}

// ---------------------------------------------------------------- actions
function fail(ev, e) { streamDeck.logger.error(`${ev.action.manifestId}: ${e.message}`); ev.action.showAlert(); }

/** Command — one ACS action from the list; hotkey defaults to the documented/suggested combo, overridable per key. */
class Command extends SingletonAction {
    manifestId = `${PLUGIN}.command`;
    onWillAppear(ev) { this.#paint(ev.action, ev.payload.settings); }
    onDidReceiveSettings(ev) { this.#paint(ev.action, ev.payload.settings); }
    async onKeyDown(ev) {
        const { hotkey } = resolve(ev.payload.settings);
        try { await sendHotkey(hotkey); } catch (e) { fail(ev, e); }
    }
    #paint(a, s) { const { cmd, hotkey } = resolve(s); a.setImage(keyImage(cmd.glyph, cmd.color, cmd.title, hotkey)); }
}
function resolve(s) {
    const cmd = CMD[s.command] ?? CMD.play;
    const hotkey = (s.hotkey ?? "").trim() || cmd.hotkey;
    return { cmd, hotkey };
}

/** Hotkey — any combo with your own title; for "Navigate to camera / view" and other actions you map in ACS yourself. */
class Hotkey extends SingletonAction {
    manifestId = `${PLUGIN}.hotkey`;
    onWillAppear(ev) { this.#paint(ev.action, ev.payload.settings); }
    onDidReceiveSettings(ev) { this.#paint(ev.action, ev.payload.settings); }
    async onKeyDown(ev) {
        const hotkey = (ev.payload.settings.hotkey ?? "").trim();
        if (!hotkey) return fail(ev, new Error("no hotkey set"));
        try { await sendHotkey(hotkey); } catch (e) { fail(ev, e); }
    }
    #paint(a, s) { a.setImage(hotkeyImage((s.title ?? "").trim(), (s.hotkey ?? "").trim(), s.color)); }
}

/** Activate — brings the ACS client window to the front so the next hotkey lands there. */
class Activate extends SingletonAction {
    manifestId = `${PLUGIN}.activate`;
    onWillAppear(ev) { ev.action.setImage(activateImage()); }
    async onKeyDown(ev) {
        const title = (ev.payload.settings.title ?? "").trim() || "AXIS Camera Station";
        try { await activateWindow(title); } catch (e) { fail(ev, e); }
    }
}

streamDeck.actions.registerAction(new Command());
streamDeck.actions.registerAction(new Hotkey());
streamDeck.actions.registerAction(new Activate());
streamDeck.connect();
