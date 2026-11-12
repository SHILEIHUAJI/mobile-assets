for f in folder.rglob("*"):

    if not f.is_file():
        continue

    # 忽略说明文件
    if f.name.lower() in {
        "readme.md",
        ".ds_store"
    }:
        continue

    files.append(
        str(
            f.relative_to(folder)
        ).replace("\\","/")
    )
