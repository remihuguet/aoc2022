from typing import List, Tuple


def parse(file: str) -> List[Tuple[str]]:
    with open(file, "r") as f:
        return [tuple(line.strip("\n").split(" ")) for line in f]


SCORE = {"A": 1, "B": 2, "C": 3, "X": 1, "Y": 2, "Z": 3}

RESULT = {0: 3, -1: 6, -2: 0, 1: 0, 2: 6}

REAL_SCORES = {"A": 1, "B": 2, "C": 3, "X": 0, "Y": 3, "Z": 6}

LOOSERS = {"A": "C", "B": "A", "C": "B"}
WINNERS = {v: k for k, v in LOOSERS.items()}


def compute_total_score(input: List[Tuple[str]]) -> int:
    return sum([SCORE[t[1]] + RESULT[int((SCORE[t[0]] - SCORE[t[1]]))] for t in input])


def compute_score_with_rules(input: List[Tuple[str]]) -> int:
    score = 0
    for t in input:
        score += REAL_SCORES[t[1]]
        if REAL_SCORES[t[1]] == 3:
            score += REAL_SCORES[t[0]]
        if REAL_SCORES[t[1]] == 0:
            score += REAL_SCORES[LOOSERS[t[0]]]
        if REAL_SCORES[t[1]] == 6:
            score += REAL_SCORES[WINNERS[t[0]]]
    return score
