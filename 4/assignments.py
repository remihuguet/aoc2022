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


def range_included(t1: Tuple[int, int], t2: Tuple[int, int]) -> bool:
    return (t1[0] >= t2[0] and t1[1] <= t2[1]) or (t1[0] <= t2[0] and t1[1] >= t2[1])


def count_ranges_included(input: List[Tuple[Tuple[int, int], Tuple[int, int]]]) -> int:
    return sum(1 for t1, t2 in input if range_included(t1, t2))


def range_overlap(t1: Tuple[int, int], t2: Tuple[int, int]) -> bool:
    return (t1[0] <= t2[0] and t2[0] <= t1[1]) or (t2[0] <= t1[0] and t2[1] >= t1[0])


def count_ranges_overlap(input: List[Tuple[Tuple[int, int], Tuple[int, int]]]) -> int:
    return sum(1 for t1, t2 in input if range_overlap(t1, t2))
