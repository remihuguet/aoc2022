from assignments import (
    parse,
    range_included,
    count_ranges_included,
    range_overlap,
    count_ranges_overlap,
)


def test_parse_file():
    assert [
        ((2, 4), (6, 8)),
        ((2, 3), (4, 5)),
        ((5, 7), (7, 9)),
        ((2, 8), (3, 7)),
        ((6, 6), (4, 6)),
        ((2, 6), (4, 8)),
    ] == parse("4/test_input.txt")


def test_range_included():
    assert not range_included((2, 4), (6, 8))
    assert not range_included((2, 3), (4, 5))
    assert not range_included((5, 7), (7, 9))
    assert range_included((2, 8), (3, 7))
    assert range_included((6, 6), (4, 6))
    assert not range_included((2, 6), (4, 8))


def test_count_ranges_included():
    assert 2 == count_ranges_included(parse("4/test_input.txt"))


def test_range_overlap():
    assert not range_overlap((2, 4), (6, 8))
    assert not range_overlap((2, 3), (4, 5))
    assert range_overlap((5, 7), (7, 9))
    assert range_overlap((2, 8), (3, 7))
    assert range_overlap((6, 6), (4, 6))
    assert range_overlap((2, 6), (4, 8))


def test_count_ranges_overlap():
    assert 4 == count_ranges_overlap(parse("4/test_input.txt"))
