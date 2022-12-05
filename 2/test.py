from shifumi import parse, compute_total_score, compute_score_with_rules


def test_parse_file():
    assert parse("2/test_input.txt") == [("A", "Y"), ("B", "X"), ("C", "Z")]


def test_total_score():
    assert compute_total_score(parse("2/test_input.txt")) == 15

    input = [("A", "Z"), ("B", "Y"), ("C", "X")]
    assert compute_total_score(input) == 15

    input = [("A", "Y"), ("B", "Z"), ("C", "X")]
    assert compute_total_score(input) == 24


def test_total_score_with_correct_rules():
    assert compute_score_with_rules(parse("2/test_input.txt")) == 12
