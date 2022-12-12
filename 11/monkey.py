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
    inspected: int = 0


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


def compute_round(monkeys: list[Monkey], supermodulo: int = None) -> list[Monkey]:
    for monkey in monkeys:
        for _ in range(len(monkey.items)):
            item = monkey.items.pop(0)
            monkey.inspected += 1
            if supermodulo:
                item = int(
                    eval(f"{item}{monkey.operation[0]}{monkey.operation[1]}")
                    % supermodulo
                )
            else:
                item = int(
                    eval(f"{item}{monkey.operation[0]}{monkey.operation[1]}") / 3
                )
            if item % monkey.test > 0:
                monkeys[monkey.target_monkey_false].items.append(item)
            else:
                monkeys[monkey.target_monkey_true].items.append(item)
    return monkeys


def compute_rounds(monkeys: list[Monkey], rounds: int) -> list[Monkey]:
    supermodulo = None
    if rounds > 20:
        supermodulo = 1
        for monkey in monkeys:
            supermodulo *= monkey.test

    for _ in range(rounds):
        monkeys = compute_round(monkeys, supermodulo=supermodulo)
    return monkeys


def compute_monkey_biz(monkeys: list[Monkey]) -> int:
    biz = sorted([monkey.inspected for monkey in monkeys])
    return biz[-1] * biz[-2]
