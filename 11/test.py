from monkey import Monkey, parse


def test_parse_input():
    assert [
        Monkey(
            id=0,
            items=[79, 98],
            operation=("*", 19),
            test=23,
            target_monkey_true=2,
            target_monkey_false=3,
        ),
        Monkey(
            id=1,
            items=[54, 65, 75, 74],
            operation=("+", 6),
            test=19,
            target_monkey_true=2,
            target_monkey_false=0,
        ),
        Monkey(
            id=2,
            items=[79, 60, 97],
            operation=("**", 2),
            test=13,
            target_monkey_true=1,
            target_monkey_false=3,
        ),
        Monkey(
            id=3,
            items=[74],
            operation=("+", 3),
            test=17,
            target_monkey_true=0,
            target_monkey_false=1,
        ),
    ] == parse("11/test_input.txt")
