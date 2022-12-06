import pytest
from tuning import compute_start_off_message, compute_start_off_packet

START_OFF_PACKET = [
    ("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 7),
    ("bvwbjplbgvbhsrlpgdmjqwftvncz", 5),
    ("nppdvjthqldpwncqszvftbrmjlhg", 6),
    ("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 10),
    ("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 11),
]


START_OFF_MESSAGES = [
    ("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 19),
    ("bvwbjplbgvbhsrlpgdmjqwftvncz", 23),
    ("nppdvjthqldpwncqszvftbrmjlhg", 23),
    ("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 29),
    ("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 26),
]


@pytest.mark.parametrize("stream, mark", START_OFF_PACKET)
def test_compute_start_off_packet(stream, mark):
    assert mark == compute_start_off_packet(stream)


@pytest.mark.parametrize("stream, mark", START_OFF_MESSAGES)
def test_compute_start_off_message(stream, mark):
    assert mark == compute_start_off_message(stream)
