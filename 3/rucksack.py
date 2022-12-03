from typing import List, Tuple


def parse(file: str) -> List[str]:
    with open(file, "r") as f:
        return [r.strip("\n") for r in f]


LETTERS = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]


def compute_total_score(input: List[str]) -> int:
    score = 0
    for line in input:
        c1, c2 = line[: len(line) // 2], line[len(line) // 2 :]
        for c in c1:
            if c in c2:
                break
        score += LETTERS.index(c) + 1
    return score


def compute_elves_groups_score(input: List[str]) -> int:
    score = 0
    breaks = []
    for i, line in enumerate(input):
        if i in breaks:
            continue
        breaks.extend([i, i + 1, i + 2])
        for c in line:
            if c in input[i + 1] and c in input[i + 2]:
                break
        score += LETTERS.index(c) + 1
    return score
