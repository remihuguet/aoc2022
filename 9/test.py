from rope import compute_knot_move, compute_tail_positions_visited, parse


def test_compute_tail_move():
    assert (0, 0) == compute_knot_move(head_knot=(0, 0), following_knot=(0, 0))
    assert (0, 0) == compute_knot_move(head_knot=(0, 1), following_knot=(0, 0))
    assert (0, 2) == compute_knot_move(head_knot=(1, 3), following_knot=(0, 2))

    assert (0, 1) == compute_knot_move(head_knot=(0, 2), following_knot=(0, 0))
    assert (1, 2) == compute_knot_move(head_knot=(2, 2), following_knot=(0, 2))

    assert (1, 3) == compute_knot_move(head_knot=(2, 3), following_knot=(0, 2))

    assert (3, 4) == compute_knot_move(head_knot=(2, 4), following_knot=(4, 3))


def test_compute_tail_positions_visited():
    assert 13 == len(compute_tail_positions_visited(parse("9/test_input.txt")))


def test_compute_tail_positions_visited_with_longer_rope():
    assert 1 == len(
        compute_tail_positions_visited(parse("9/test_input.txt"), rope_length=10)
    )
    assert 36 == len(
        compute_tail_positions_visited(parse("9/test_input_2.txt"), rope_length=10)
    )
