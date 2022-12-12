from monkey import Monkey, parse, compute_round, compute_rounds, compute_monkey_biz


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


def test_compute_one_round():
    monkeys = parse("11/test_input.txt")

    round_1_monkeys = compute_round(monkeys)

    assert round_1_monkeys[0].items == [20, 23, 27, 26]
    assert round_1_monkeys[1].items == [2080, 25, 167, 207, 401, 1046]
    assert round_1_monkeys[2].items == []
    assert round_1_monkeys[3].items == []


def test_compute_monkey_business():
    monkeys = parse("11/test_input.txt")
    monkeys = compute_rounds(monkeys, 20)
    assert 10605 == compute_monkey_biz(monkeys)


def test_long_biz():
    monkeys = parse("11/test_input.txt")
    monkeys = compute_rounds(monkeys, 10000)
    assert 2713310158 == compute_monkey_biz(monkeys)
