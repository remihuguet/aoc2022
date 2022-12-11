import math


def compute_knot_move(
    head_knot: tuple[int, int], following_knot: tuple[int, int]
) -> tuple[int, int]:
    dx, dy = head_knot[0] - following_knot[0], head_knot[1] - following_knot[1]
    if math.sqrt(dx**2 + dy**2) <= math.sqrt(2):
        return following_knot
    else:
        new_tail = list(following_knot)
        new_tail[0] += int(dx / abs(dx)) if dx != 0 else 0
        new_tail[1] += int(dy / abs(dy)) if dy != 0 else 0
        return tuple(new_tail)


def parse(file: str) -> list[tuple[str, int]]:
    with open(file, "r") as f:
        return [
            (line.strip().split(" ")[0], int(line.strip().split(" ")[-1]))
            for line in f.readlines()
        ]


DIRECTION_TO_VECTOR = {
    "R": (1, 0),
    "L": (-1, 0),
    "U": (0, 1),
    "D": (0, -1),
}


def compute_tail_positions_visited(
    movements: list[tuple[str, int]], rope_length: int = 2
) -> set[tuple[int, int]]:
    positions = set()
    knots = [(0, 0) for k in range(rope_length)]
    for direction, distance in movements:
        for i in range(distance):
            knots[0] = (
                knots[0][0] + DIRECTION_TO_VECTOR[direction][0],
                knots[0][1] + DIRECTION_TO_VECTOR[direction][1],
            )
            for i, knot in enumerate(knots):
                if i == 0:
                    continue
                knots[i] = compute_knot_move(knots[i - 1], knot)
            positions.add(knots[-1])
    return positions
