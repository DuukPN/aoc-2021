from lib import load_input

day = 7


def solve(data, part=2):
    lines = [int(x) for x in data.split(",")]
    if part == 1:
        return part_one(lines)
    elif part == 2:
        return part_two(lines)


def part_one(data):
    return min([sum(abs(i - x) for x in data) for i in range(min(data), max(data) + 1)])


def part_two(data):
    return min([sum([(abs(i - x) * (abs(i - x) + 1)) // 2 for x in data]) for i in range(min(data), max(data) + 1)])


if __name__ == "__main__":
    print(solve(load_input(day), 1))
    print(solve(load_input(day)))
