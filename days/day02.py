from lib import read_input


def solve(data):
    # return part_one(data)
    return part_two(data)


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
    print(solve(read_input(2)))
