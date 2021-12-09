from lib import load_input

day = 9


def solve(data, part=2):
    lines = data.splitlines()
    if part == 1:
        return part_one(lines)
    elif part == 2:
        return part_two(lines)


def part_one(data):
    low_points = []
    for i, line in enumerate(data):
        for j, c in enumerate(line):
            num = int(c)
            neighbors = []
            if i != 0:
                neighbors.append(data[i - 1][j])
            if i != len(data) - 1:
                neighbors.append(data[i + 1][j])
            if j != 0:
                neighbors.append(data[i][j - 1])
            if j != len(data[i]) - 1:
                neighbors.append(data[i][j + 1])

            if all([int(n) > num for n in neighbors]):
                low_points.append(num)

    return sum(low_points) + len(low_points)


def part_two(data):
    taken = [[False] * len(data[0]) for _ in range(len(data))]
    neighbors = []
    basins = []
    basin = -1
    while not all([all(line) for line in taken]):
        if len(neighbors) == 0:
            i, j = 0, 0
            while taken[i][j]:
                i += 1
                if i == len(data):
                    i = 0
                    j += 1
            basin += 1
            basins.append(0)
        else:
            i, j = neighbors.pop()

        if taken[i][j]:
            continue

        taken[i][j] = True

        if data[i][j] == "9":
            continue

        basins[basin] += 1

        if i != 0 and not taken[i - 1][j]:
            neighbors.append((i-1, j))
        if i != len(data) - 1 and not taken[i + 1][j]:
            neighbors.append((i+1, j))
        if j != 0 and not taken[i][j - 1]:
            neighbors.append((i, j-1))
        if j != len(data[i]) - 1 and not taken[i][j + 1]:
            neighbors.append((i, j+1))

    basins.sort(reverse=True)
    return basins[0] * basins[1] * basins[2]


if __name__ == "__main__":
    print(solve(load_input(day), 1))
    print(solve(load_input(day)))
