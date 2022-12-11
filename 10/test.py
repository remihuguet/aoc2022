from cpu import compute_register, parse, compute_strength_at, compute_sum

SMALL = ["noop", "addx 3", "addx -5"]


def test_compute_register():
    assert [1, 1, 1, 4, 4, -1] == compute_register(SMALL)


def test_compute_strength_at():
    register = compute_register(parse("10/test_input.txt"))
    assert 420 == compute_strength_at(register, 20)
    assert 1140 == compute_strength_at(register, 60)
    assert 1800 == compute_strength_at(register, 100)
    assert 2940 == compute_strength_at(register, 140)
    assert 2880 == compute_strength_at(register, 180)
    assert 3960 == compute_strength_at(register, 220)


def test_compute_sum():
    assert 13140 == compute_sum("10/test_input.txt")
