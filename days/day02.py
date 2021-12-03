from lib import load_input

day = X


def solve(data, part=2):
    lines = data.splitlines()
    if part == 1:
        return part_one(lines)
    elif part == 2:
        return part_two(lines)


def part_one(data):
    depth = 0
    forward = 0
    for line in data:
        instr = line.split(" ")
        if instr[0] == "down":
            depth += int(instr[1])
        elif instr[0] == "up":
            depth -= int(instr[1])
        else:
            forward += int(instr[1])
    return depth * forward


def part_two(data):
    aim = 0
    depth = 0
    forward = 0
    for line in data:
        instr = line.split(" ")
        if instr[0] == "down":
            aim += int(instr[1])
        elif instr[0] == "up":
            aim -= int(instr[1])
        else:
            depth += aim * int(instr[1])
            forward += int(instr[1])
    return depth * forward


if __name__ == "__main__":
    data = load_input(day)
    print(solve(data, 1))
    print(solve(data))