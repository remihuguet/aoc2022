def parse(file: str) -> list[str]:
    with open(file, "r") as f:
        return [line.strip() for line in f.readlines()]


def compute_register(operations: list[str]) -> list[int]:
    register = [1]
    for operation in operations:
        register.append(register[-1])
        if "addx" in operation:
            register.append(register[-1] + int(operation.split(" ")[1]))
    return register


def compute_strength_at(register: list[int], cycle: int) -> int:
    return register[cycle - 1] * cycle


def compute_sum(
    file: str, for_cycle: list[int] = [20 + i * 40 for i in range(6)]
) -> int:
    register = compute_register(parse(file))
    return sum(compute_strength_at(register, cycle) for cycle in for_cycle)


def crt(file: str):
    register = compute_register(parse(file))
    cycle = 0
    for line in range(6):
        line = []
        for col in range(40):
            sprite = register[cycle]
            if col in (sprite - 1, sprite, sprite + 1):
                line.append("#")
            else:
                line.append(".")
            cycle += 1
        print("".join(line))
