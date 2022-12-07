from fs import parse, compute_total_size, compute_dir_size_to_free


def test_parse_input():
    assert {
        "/": {
            "a": {"e": {"i": 584}, "f": 29116, "g": 2557, "h.lst": 62596},
            "b.txt": 14848514,
            "c.dat": 8504156,
            "d": {"j": 4060174, "d.log": 8033020, "d.ext": 5626152, "k": 7214296},
        }
    } == parse("7/test_input.txt")


def test_compute_total_size():
    fs = parse("7/test_input.txt")

    assert 95437 == compute_total_size(fs, max_size=100000)


def test_dir_size_to_delete():
    fs = parse("7/test_input.txt")
    assert 24933642 == compute_dir_size_to_free(fs)
