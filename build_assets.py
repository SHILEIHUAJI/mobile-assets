import json
from pathlib import Path

ROOT = Path(__file__).parent

IGNORE = {
    ".git",
    ".github",
    "__pycache__"
}

result = {}

for item in ROOT.iterdir():

    if not item.is_dir():
        continue

    if item.name in IGNORE:
        continue

    files = []

    for f in item.rglob("*"):

        if f.is_file():
            files.append(
                str(
                    f.relative_to(item)
                ).replace("\\", "/")
            )

    result[item.name] = {
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

print("资产清单已生成")
