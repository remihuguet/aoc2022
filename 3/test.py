from rucksack import parse, compute_total_score, compute_elves_groups_score


def test_parse_file():
    assert [
        "vJrwpWtwJgWrhcsFMMfFFhFp",
        "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
        "PmmdzqPrVvPwwTWBwg",
        "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
        "ttgJtRGJQctTZtZT",
        "CrZsJsPPZsGzwwsLwLmpwMDw",
    ] == parse("3/test_input.txt")


def test_compute_total_rucksacks_score():
    assert 157 == compute_total_score(parse("3/test_input.txt"))


def test_compute_elves_groups_score():
    assert 70 == compute_elves_groups_score(parse("3/test_input.txt"))
