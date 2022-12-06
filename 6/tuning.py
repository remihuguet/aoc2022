def compute_start_off_packet(stream: str) -> int:
    return _compute_start_off(stream, 4)


def compute_start_off_message(stream: str) -> int:
    return _compute_start_off(stream, 14)


def _compute_start_off(stream: str, size: int) -> int:
    mark = list(stream[:size])
    for i, c in enumerate(stream[size:]):
        if len(set(mark)) == size:
            break
        mark.pop(0)
        mark.append(c)
    return i + size
