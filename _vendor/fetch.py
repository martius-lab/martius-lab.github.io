"""
download third-party fonts, icons, and scripts into assets/vendor, so the site
doesn't make requests to external servers (Google Fonts, Font Awesome, unpkg)

run from repo root: python3 _vendor/fetch.py
"""

import re
import shutil
import urllib.request
from pathlib import Path

out = Path("assets/vendor")

# fonts used in _styles/-theme.scss, with weights used there
fonts = ["Barlow", "Roboto Mono"]
weights = [200, 400, 500, 600]
subsets = ["latin", "latin-ext"]

fontawesome = "https://cdn.jsdelivr.net/npm/@fortawesome/fontawesome-free@6.7.0"

scripts = {
    "popper.min.js": "https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.8/dist/umd/popper.min.js",
    "tippy.min.js": "https://cdn.jsdelivr.net/npm/tippy.js@6.3.7/dist/tippy-bundle.umd.min.js",
    "mark.min.js": "https://cdn.jsdelivr.net/npm/mark.js@8.11.1/dist/mark.min.js",
    "pygments.css": "https://cdn.jsdelivr.net/gh/StylishThemes/Syntax-Themes/pygments/css-github/pygments-tomorrow-night-eighties.css",
}

# modern user agent, so google serves woff2
agent = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36"


def get(url):
    request = urllib.request.Request(url, headers={"User-Agent": agent})
    with urllib.request.urlopen(request) as response:
        return response.read()


def fetch_fonts():
    folder = out / "fonts"
    folder.mkdir(parents=True, exist_ok=True)
    families = "&".join(
        f"family={font.replace(' ', '+')}:ital,wght@"
        + ";".join(f"{i},{w}" for i in [0, 1] for w in weights)
        for font in fonts
    )
    css = get(f"https://fonts.googleapis.com/css2?{families}&display=swap").decode()

    # keep only wanted subsets ("/* latin */" comment precedes each @font-face)
    blocks = re.findall(r"/\* ([\w-]+) \*/\s*(@font-face \{.*?\})", css, re.S)
    result = []
    for subset, block in blocks:
        if subset not in subsets:
            continue
        url = re.search(r"url\((.*?)\)", block).group(1)
        family = re.search(r"font-family: '(.*?)'", block).group(1)
        style = re.search(r"font-style: (\w+)", block).group(1)
        weight = re.search(r"font-weight: (\d+)", block).group(1)
        name = f"{family.replace(' ', '-').lower()}-{weight}-{style}-{subset}.woff2"
        (folder / name).write_bytes(get(url))
        result.append(f"/* {subset} */\n" + block.replace(url, name))
    (folder / "fonts.css").write_text("\n".join(result) + "\n")
    print(f"{len(result)} font faces")


def fetch_fontawesome():
    folder = out / "fontawesome"
    shutil.rmtree(folder, ignore_errors=True)
    (folder / "css").mkdir(parents=True)
    (folder / "webfonts").mkdir()
    css = get(f"{fontawesome}/css/all.min.css").decode()
    (folder / "css" / "all.min.css").write_text(css)
    for name in sorted(set(re.findall(r"\.\./webfonts/([\w.-]+)", css))):
        (folder / "webfonts" / name).write_bytes(get(f"{fontawesome}/webfonts/{name}"))
    print("font awesome")


def fetch_scripts():
    for name, url in scripts.items():
        (out / name).write_bytes(get(url))
    print(f"{len(scripts)} scripts/styles")


out.mkdir(parents=True, exist_ok=True)
fetch_fonts()
fetch_fontawesome()
fetch_scripts()
