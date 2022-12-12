import dataclasses
from typing import Optional


@dataclasses.dataclass
class Monkey:
    id: Optional[int]
    items: Optional[list[int]]
    test: Optional[int]
    operation: Optional[tuple[str, int]]
    target_monkey_true: Optional[int]
    target_monkey_false: Optional[int]


def parse(file: str) -> list[Monkey]:
    with open(file, "r") as f:
        monkeys = []
        for line in f.readlines():
            if line.startswith("  Operation"):
                if "old * old" in line:
                    operation = ("**", 2)
                else:
                    operation = (line.split(" ")[-2], int(line.split(" ")[-1]))
            elif line.startswith("  Starting"):
                items = [int(item) for item in line.split(":")[1].split(",")]
            elif line.startswith("  Test"):
                test = int(line.split(" ")[-1])
            elif line.startswith("    If true"):
                target_monkey_true = int(line.split(" ")[-1])
            elif line.startswith("    If false"):
                target_monkey_false = int(line.split(" ")[-1])
                monkeys.append(
                    Monkey(
                        id=id,
                        items=items,
                        operation=operation,
                        test=test,
                        target_monkey_false=target_monkey_false,
                        target_monkey_true=target_monkey_true,
                    )
                )
            elif line.startswith("Monkey"):
                id = int(line[-3])
    return monkeys
