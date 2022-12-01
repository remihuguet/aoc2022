from typing import List, Tuple

def parse(file: str) -> List[Tuple[int]]:
    with open(file, "r") as f:
        input, current = [], []
        for l in f:
            l = l.strip("\n")
            if l != "":
                current.append(int(l))
            else:
                if current:
                    input.append(tuple(current))
                current = []
    return input

def find_max_calories_carried(input: List[Tuple[int]]) -> int:
    return max([sum(meal) for meal in input])


def find_top_three_calories(input: List[Tuple[int]]) -> int:
    return sum(sorted([sum(meal) for meal in input], reverse=True)[:3])