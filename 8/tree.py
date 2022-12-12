from typing import List


def parse(file: str) -> List[List[int]]:
    with open(file, "r") as f:
        return [[int(x) for x in line.strip()] for line in f]


def is_tree_visible(map: List[List[int]], line: int, column: int) -> bool:
    if line in (0, len(map) - 1) or column in (0, len(map[0]) - 1):
        return True

    height = map[line][column]
    if _check(line + 1, len(map), [map[i][column] for i in range(len(map))], height):
        return True
    if _check(0, line, [map[i][column] for i in range(len(map))], height):
        return True
    if _check(column + 1, len(map[0]), map[line], height):
        return True
    if _check(0, column, map[line], height):
        return True

    return False


def _check(start: int, end: int, row: List[int], height: int):
    for i in range(start, end):
        if row[i] >= height:
            return False
    return True


def count_visible_trees(map: List[List[int]]) -> int:
    return sum(
        1
        for line in range(len(map))
        for column in range(len(map[0]))
        if is_tree_visible(map, line, column)
    )


def compute_tree_score(map: List[List[int]], line: int, column: int) -> int:
    height = map[line][column]
    score = 1

    score *= _compute_score(
        line + 1, len(map), [map[i][column] for i in range(len(map))], height
    )
    score *= _compute_score(
        0, line, [map[i][column] for i in range(len(map))], height, reversed=True
    )
    score *= _compute_score(column + 1, len(map[0]), map[line], height)
    score *= _compute_score(0, column, map[line], height, reversed=True)
    return score


def _compute_score(start: int, end: int, row: List[int], height: int, reversed=False):
    score = 0
    if reversed:
        r = sorted(list(range(start, end)), reverse=True)
    else:
        r = list(range(start, end))
    for i in r:
        score += 1
        if row[i] >= height:
            break
    return score


def compute_max_tree_score(map: List[List[int]]) -> int:
    return max(
        compute_tree_score(map, line, column)
        for line in range(len(map))
        for column in range(len(map[0]))
    )
