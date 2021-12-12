from lib import load_input


def solve(data, part=2):
    lines = data.splitlines()
    if part == 1:
        return part_one(lines)
    elif part == 2:
        return part_two(lines)


def part_one(data):
    low_points = get_low_points(data)
    total = 0
    for i, j in low_points:
        total += int(data[i][j]) + 1

    return total


def part_two(data):
    taken = [[False] * len(data[0]) for _ in range(len(data))]
    basins = []
    for basin, p in enumerate(get_low_points(data)):
        neighbors = [p]
        basins.append(0)
        while neighbors:
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


def get_low_points(data):
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
                low_points.append((i, j))
    return low_points


if __name__ == "__main__":
    print(solve(load_input(), 1))
    print(solve(load_input()))
