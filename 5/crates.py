from typing import List, Tuple


def parse(file: str) -> List[str]:
    with open(file, "r") as f:
        return [
            (
                tuple(
                    tuple(int(i) for i in a.split("-"))
                    for a in r.strip("\n").split(",")
                )
            )
            for r in f
        ]
