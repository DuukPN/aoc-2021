from lib import load_input

day = 7


def solve(data, part=2):
    lines = [int(x) for x in data.split(",")]
    if part == 1:
        return part_one(lines)
    elif part == 2:
        return part_two(lines)


def part_one(data):
    min_fuel = float("inf")
    for i in range(min(data), max(data) + 1):
        delta = 0
        for x in data:
            delta += abs(i - x)
        if delta < min_fuel:
            min_fuel = delta
    return min_fuel


def part_two(data):
    min_fuel = float("inf")
    for i in range(min(data), max(data) + 1):
        delta = 0
        for x in data:
            delta += (abs(i - x) * (abs(i - x) + 1)) / 2
        if delta < min_fuel:
            min_fuel = delta
    return min_fuel


if __name__ == "__main__":
    print(solve(load_input(day), 1))
    print(solve(load_input(day)))
