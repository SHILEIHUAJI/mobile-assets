import json
from pathlib import Path

ROOT = Path(__file__).parent

IGNORE_DIRS = {
    ".git",
    ".github",
    "__pycache__"
}

IGNORE_FILES = {
    "readme.md",
    ".ds_store"
}

result = {}

for folder in ROOT.iterdir():

    if not folder.is_dir():
        continue

    if folder.name in IGNORE_DIRS:
        continue

    files = []

    for f in folder.rglob("*"):

        if not f.is_file():
            continue

        if f.name.lower() in IGNORE_FILES:
            continue

        files.append(
            str(
                f.relative_to(folder)
            ).replace("\\", "/")
        )

    result[folder.name] = {
        "count": len(files),
        "files": sorted(files)
    }

with open(
    ROOT / "assets.json",
    "w",
    encoding="utf-8"
) as fp:

    json.dump(
        result,
        fp,
        ensure_ascii=False,
        indent=2
    )

print("assets.json 已生成")
