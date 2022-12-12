import pytest
from tree import parse, is_tree_visible, count_visible_trees, compute_tree_score,compute_max_tree_score


def test_parse():
    assert parse("8/test_input.txt") == [
        [3, 0, 3, 7, 3],
        [2, 5, 5, 1, 2],
        [6, 5, 3, 3, 2],
        [3, 3, 5, 4, 9],
        [3, 5, 3, 9, 0],
    ]


TREES = [
    (0, 0, True),
    (0, 1, True),
    (0, 2, True),
    (4, 4, True),
    (4, 3, True),
    (1, 1, True),
    (1, 2, True),
    (1, 3, False),
    (2, 1, True),
    (2, 2, False),
    (2, 3, True),
    (3, 1, False),
    (3, 2, True),
    (3, 3, False),
]


@pytest.mark.parametrize(("line", "column", "expected"), TREES)
def test_is_tree_visible(line, column, expected):
    map = parse("8/test_input.txt")

    assert is_tree_visible(map, line, column) == expected


def test_count_visible_trees():
    map = parse("8/test_input.txt")
    assert count_visible_trees(map) == 21


def test_tree_score():
    map = parse("8/test_input.txt")

    assert compute_tree_score(map, 1, 2) == 4
    assert compute_tree_score(map, 3, 2) == 8

def test_max_tree_score():
    map = parse("8/test_input.txt")
    assert compute_max_tree_score(map) == 8