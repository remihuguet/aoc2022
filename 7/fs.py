def parse(file: str) -> dict:
    with open(file, "r") as f:
        fs = {}
        positions = []
        current_dir = None
        for line in f:
            line = line.strip("\n")
            if line.startswith("$"):
                if line.split(" ")[1] == "cd":
                    if line.split(" ")[2] == "..":
                        positions.pop()
                    else:
                        positions.append(line.split(" ")[2])
            else:
                current_dir = _get_current_dir(fs, positions)
                current_dir[line.split(" ")[1]] = (
                    {} if line.startswith("dir") else int(line.split(" ")[0])
                )
    return fs


def _get_current_dir(fs: dict, positions: list) -> dict:
    current_dir = fs
    for p in positions:
        if p in current_dir:
            current_dir = current_dir[p]
        else:
            current_dir[p] = {}
            current_dir = current_dir[p]
    return current_dir


def compute_dir_size(fs: dict, dir_sizes: list) -> int:
    dir_size = 0
    for k, v in fs.items():
        if isinstance(v, dict):
            dir_size += compute_dir_size(v, dir_sizes)
        else:
            dir_size += v
    dir_sizes.append(dir_size)
    return dir_size


def compute_total_size(fs: dict, max_size: int) -> int:
    dir_sizes = []
    compute_dir_size(fs, dir_sizes)
    return sum([d for d in dir_sizes if d <= max_size])


def compute_dir_size_to_free(fs: dict) -> int:
    dir_sizes = []
    compute_dir_size(fs, dir_sizes)
    needed_space = 30_000_000 - 70_000_000 + dir_sizes[-1]
    for d in sorted(dir_sizes):
        if d >= needed_space:
            return d
