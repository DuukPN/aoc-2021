from lib import load_input
from collections import defaultdict


def solve(data, part=2):
    lines = [int(x) for x in data.split(",")]
    if part == 1:
        return part_one(lines)
    elif part == 2:
        return part_two(lines)


def part_one(data):
    return population(data, 80)


def part_two(data):
    return population(data, 256)


def population(data, days):
    fish = [0] * 9
    for x in data:
        fish[x] += 1

    for i in range(days):
        hatched = fish[0]
        for j in range(8):
            fish[j] = fish[j + 1]
        fish[6] += hatched
        fish[8] = hatched

    return sum(fish)


def naive_population(data, days):
    my_data = data
    for i in range(days):
        for x in range(len(my_data)):
            if my_data[x] == 0:
                my_data[x] = 7
                my_data.append(8)
            my_data[x] -= 1

    return len(my_data)


if __name__ == "__main__":
    print(solve(load_input(), 1))
    print(solve(load_input()))
