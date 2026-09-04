#!/usr/bin/env python3
"""Builds the three bundled profiles (Stream Deck 7 v3 format) for Deck for AXIS Camera Station Pro & 5.
Pavel Kotyza <kotyza@gmail.com> — https://www.4xs.dev
"""
import json, os, shutil, uuid, zipfile

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "build")
PLUGIN = {"Name": "Deck for AXIS Camera Station Pro & 5", "UUID": "com.4xsdev.acs-pro", "Version": "1.0.0.0"}
UUID = "com.4xsdev.acs-pro"

def C(command): return dict(uuid=f"{UUID}.command", name="ACS Command", settings={"command": command}, img=command)
def H(title, hotkey, color="camera"):
    return dict(uuid=f"{UUID}.hotkey", name="ACS Hotkey", settings={"title": title, "hotkey": hotkey, "color": color},
                img="hotkey-" + title.lower().replace(" ", "-"))
def A(): return dict(uuid=f"{UUID}.activate", name="Activate ACS", settings={}, img="activate")

# Model codes: 20GAA9902 = Stream Deck MK.2 (15 keys), 20GAI9901 = Mini (6), 20GAT9901 = XL (32).
LAYOUTS = {
    "ACS Pro": dict(model="20GAA9902", device_type=0, cols=5, rows=3, keys={
        "0,0": C("prev"), "1,0": C("step-back"), "2,0": C("play"), "3,0": C("step-fwd"), "4,0": C("next"),
        "0,1": C("bookmark"), "1,1": C("live-rec"), "2,1": C("prev-cam"), "3,1": C("next-cam"), "4,1": A(),
        "0,2": C("preset-1"), "1,2": C("preset-2"), "2,2": C("preset-3"), "3,2": C("preset-4"), "4,2": C("hotkeys"),
    }),
    "ACS Pro Mini": dict(model="20GAI9901", device_type=1, cols=3, rows=2, keys={
        "0,0": C("prev"), "1,0": C("play"), "2,0": C("next"),
        "0,1": C("bookmark"), "1,1": C("live-rec"), "2,1": C("next-cam"),
    }),
    "ACS Pro XL": dict(model="20GAT9901", device_type=2, cols=8, rows=4, keys={
        "0,0": C("prev"), "1,0": C("step-back"), "2,0": C("play"), "3,0": C("step-fwd"), "4,0": C("next"), "5,0": C("marker"), "6,0": C("bookmark"), "7,0": C("live-rec"),
        "0,1": C("preset-1"), "1,1": C("preset-2"), "2,1": C("preset-3"), "3,1": C("preset-4"), "4,1": C("zoom-out"), "5,1": C("zoom-in"), "6,1": C("focus-near"), "7,1": C("focus-far"),
        "0,2": C("prev-cam"), "1,2": C("next-cam"), "2,2": C("prev-tab"), "3,2": C("next-tab"), "4,2": C("prev-cell"), "5,2": C("next-cell"), "6,2": C("views"), "7,2": C("fullscreen-exit"),
        "0,3": H("Camera 1", "Ctrl+5"), "1,3": H("Camera 2", "Ctrl+6"), "2,3": H("Camera 3", "Ctrl+7"), "3,3": H("View 1", "Ctrl+8"),
        "4,3": A(), "5,3": C("hotkeys"), "6,3": C("config"), "7,3": C("help"),
    }),
}

def action(spec):
    return {"ActionID": str(uuid.uuid4()), "LinkedTitle": True, "Resources": None, "State": 0,
            "Name": spec["name"], "UUID": spec["uuid"], "Plugin": PLUGIN, "Settings": spec["settings"],
            "States": [{"FontFamily": "", "FontSize": 12, "FontStyle": "", "FontUnderline": False,
                        "OutlineThickness": 2, "ShowTitle": False, "TitleAlignment": "middle", "TitleColor": "#ffffff"}]}

def build(name, layout):
    shutil.rmtree(OUT, ignore_errors=True)
    prof, page = str(uuid.uuid4()).upper(), str(uuid.uuid4()).upper()
    root = os.path.join(OUT, f"{prof}.sdProfile"); pdir = os.path.join(root, "Profiles", page)
    os.makedirs(os.path.join(pdir, "Images")); os.makedirs(os.path.join(root, "Images"))
    json.dump({"Controllers": [{"Actions": {k: action(v) for k, v in layout["keys"].items()}, "Type": "Keypad"}], "Icon": "", "Name": ""},
              open(os.path.join(pdir, "manifest.json"), "w"), indent=2)
    json.dump({"Device": {"Model": layout["model"], "UUID": ""}, "Name": name,
               "Pages": {"Current": page.lower(), "Default": page.lower(), "Pages": [page.lower()]}, "Version": "3.0"},
              open(os.path.join(root, "manifest.json"), "w"), indent=2)
    z = os.path.join(HERE, f"{name}.streamDeckProfile")
    with zipfile.ZipFile(z, "w", zipfile.ZIP_DEFLATED) as zf:
        for dp, _, fs in os.walk(root):
            for f in fs: zf.write(os.path.join(dp, f), os.path.relpath(os.path.join(dp, f), OUT))
    print("wrote", z)

if __name__ == "__main__":
    for n, l in LAYOUTS.items(): build(n, l)
    shutil.rmtree(OUT, ignore_errors=True)
