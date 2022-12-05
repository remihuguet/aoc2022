from typing import Dict, Any


def parse(file: str) -> Dict[str, Any]:
    with open(file, "r") as f:
        raw_stacks, instructions = [], []
        for line in f:
            if line.startswith("move"):
                instr = line.split(" ")
                instructions.append((int(instr[1]), int(instr[3]), int(instr[5])))
            else:
                raw_stacks.append(line)
        raw_stacks.pop()
        num_stacks = int(raw_stacks.pop().split(" ")[-2])
        stacks = [[] for _ in range(num_stacks)]
        for i in reversed(range(num_stacks)):
            for rs in reversed(raw_stacks):
                if rs[4 * i + 1] not in [" ", "]", "[", "\n"]:
                    stacks[i].append(rs[4 * i + 1])
    return {
        "stacks": stacks,
        "instructions": instructions,
    }


def process_move(input: Dict[str, Any]) -> str:
    stacks = input["stacks"]
    instructions = input["instructions"]
    for instr in instructions:
        for _ in range(instr[0]):
            stacks[instr[2] - 1].append(stacks[instr[1] - 1].pop())
    return "".join([s[-1] for s in stacks])


def process_move_9001(input: Dict[str, Any]) -> str:
    stacks = input["stacks"]
    instructions = input["instructions"]
    for instr in instructions:
        stacks[instr[2] - 1].extend(stacks[instr[1] - 1][-instr[0] :])
        for _ in range(instr[0]):
            stacks[instr[1] - 1].pop()
    return "".join([s[-1] for s in stacks])
