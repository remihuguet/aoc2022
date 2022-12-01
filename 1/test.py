from calories import find_max_calories_carried, parse, find_top_three_calories

def test_parse_file():
    assert [(1000, 2000, 3000), (4000,), (5000, 6000), (7000, 8000, 9000), (10000,)] == parse("1/test_input.txt")


def test_most_calories():
    input = parse("1/test_input.txt")
    assert find_max_calories_carried(input) == 24000

    input = [(0,), (100,)]
    assert find_max_calories_carried(input) == 100

    input = [(0,)]
    assert find_max_calories_carried(input) == 0


def test_top_three_calories():

    input = [(0,), (100,), (100, 200), (50, 100)]
    assert find_top_three_calories(input) == 550

    input = [(0,)]
    assert find_top_three_calories(input) == 0
    input = parse("1/test_input.txt")
    assert find_top_three_calories(input) == 45000
