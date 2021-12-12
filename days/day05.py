from lib import load_input
import numpy as np


def solve(data, part=2):
    lines = [[x[0].split(","), x[1].split(",")] for x in [line.split(" -> ") for line in data.splitlines()]]
    if part == 1:
        return part_one(lines)
    elif part == 2:
        return part_two(lines)


def part_one(data):
    return count_double_vents(data)


def part_two(data):
    return count_double_vents(data, True)


def count_double_vents(data, diagonal=False):
    field = np.zeros(1000000).reshape((1000, 1000))
    for line in data:
        x1 = int(line[0][0])
        x2 = int(line[1][0])
        y1 = int(line[0][1])
        y2 = int(line[1][1])
        if x1 == x2:
            if y1 > y2:
                field[x1, y2: y1 + 1] += 1
            else:
                field[x1, y1: y2 + 1] += 1

        elif y1 == y2:
            if x1 > x2:
                field[x2: x1 + 1, y1] += 1
            else:
                field[x1: x2 + 1, y1] += 1

        elif diagonal:
            dx = x2 - x1
            dy = y2 - y1
            top = max(x1, x2)
            bottom = min(x1, x2)
            if dy == dx:
                y = min(y1, y2)
                for i in range(0, top-bottom+1):
                    field[bottom + i, y + i] += 1
            else:
                coordinate_sum = x1 + y1
                for i in range(bottom, top + 1):
                    field[i, coordinate_sum - i] += 1

    return (field >= 2).sum()


if __name__ == "__main__":
    print(solve(load_input(), 1))
    print(solve(load_input()))
