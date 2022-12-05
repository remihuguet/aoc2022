from crates import parse, process_move, process_move_9001


def test_parse_file():
    assert {
        "stacks": [
            ["Z", "N"],
            ["M", "C", "D"],
            ["P"],
        ],
        "instructions": [(1, 2, 1), (3, 1, 3), (2, 2, 1), (1, 1, 2)],
    } == parse("5/test_input.txt")


def test_process_move():
    assert "CMZ" == process_move(parse("5/test_input.txt"))

def test_process_move_9001():
    assert "MCD" == process_move_9001(parse("5/test_input.txt"))