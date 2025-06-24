import dataclasses

import downloader


@dataclasses.dataclass
class Folder:
    non_deletable: int
    deletable: int
    subfolders: list[int]


def is_deletable(name: str) -> bool:
    return "delete" in name or "temporary" in name


def get_deletion_size(
    i: int, do_delete: int, folders: list[Folder], deletable_folders: set[int]
) -> int:
    folder = folders[i]

    if i in deletable_folders:
        do_delete = True

    result = folder.deletable
    if do_delete:
        result += folder.non_deletable

    for subfolder in folder.subfolders:
        result += get_deletion_size(subfolder, do_delete, folders, deletable_folders)

    return result


# with open("./2024/input/03-12.txt") as f:
# lines = f.read().splitlines()

# Puzzle 34 uses different url
lines = downloader.get(
    "https://codingquest.io/2024/day07_files_to_scan.txt", "34.txt", True
).splitlines()


folders = []
deletable_folders = set()
lines.reverse()
while lines:
    folder = Folder(non_deletable=0, deletable=0, subfolders=[])
    lines.pop()
    while lines and lines[-1].startswith(" - "):
        parts = lines.pop()[3:].split()

        if len(parts) == 2:
            name, size_str = parts
            size = int(size_str)
            if is_deletable(name):
                folder.deletable += size
            else:
                folder.non_deletable += size
            continue

        subfolder_id = int(parts[-1][:-1])
        subfolder_name = parts[0]

        folder.subfolders.append(subfolder_id)
        if is_deletable(subfolder_name):
            deletable_folders.add(subfolder_id)

    folders.append(folder)


answer = get_deletion_size(0, False, folders, deletable_folders)
print(answer)
