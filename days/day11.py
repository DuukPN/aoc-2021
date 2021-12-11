from lib import load_input

day = 11


def solve(data, part=2):
    lines = [[int(c) for c in line] for line in data.splitlines()]
    if part == 1:
        return part_one(lines)
    elif part == 2:
        return part_two(lines)


def part_one(data):
    flashes = 0
    for _ in range(100):
        flashing = gain_energy(data)
        flashed = [[False] * len(data[0]) for _ in range(len(data))]
        while len(flashing) > 0:
            flashes += 1
            charge_neighbors(data, flashed, flashing)

    return flashes


def part_two(data):
    for step in range(1000):
        flashing = gain_energy(data)
        flashed = [[False] * len(data[0]) for _ in range(len(data))]
        while len(flashing) > 0:
            charge_neighbors(data, flashed, flashing)

        if all([all(line) for line in flashed]):
            return step+1

    return -1


def gain_energy(data):
    flashing = []
    for i in range(len(data)):
        for j in range(len(data[0])):
            data[i][j] += 1
            if data[i][j] == 10:
                flashing.append((i, j))

    return flashing


def charge_neighbors(data, flashed, flashing):
    i, j = flashing.pop()
    data[i][j] = 0
    flashed[i][j] = True
    if i - 1 >= 0 and not flashed[i - 1][j]:
        data[i - 1][j] += 1
        if data[i - 1][j] == 10:
            flashing.append((i - 1, j))
    if i - 1 >= 0 and j - 1 >= 0 and not flashed[i - 1][j - 1]:
        data[i - 1][j - 1] += 1
        if data[i - 1][j - 1] == 10:
            flashing.append((i - 1, j - 1))
    if j - 1 >= 0 and not flashed[i][j - 1]:
        data[i][j - 1] += 1
        if data[i][j - 1] == 10:
            flashing.append((i, j - 1))
    if i + 1 < len(data) and j - 1 >= 0 and not flashed[i + 1][j - 1]:
        data[i + 1][j - 1] += 1
        if data[i + 1][j - 1] == 10:
            flashing.append((i + 1, j - 1))
    if i + 1 < len(data) and not flashed[i + 1][j]:
        data[i + 1][j] += 1
        if data[i + 1][j] == 10:
            flashing.append((i + 1, j))
    if i + 1 < len(data) and j + 1 < len(data[0]) and not flashed[i + 1][j + 1]:
        data[i + 1][j + 1] += 1
        if data[i + 1][j + 1] == 10:
            flashing.append((i + 1, j + 1))
    if j + 1 < len(data[0]) and not flashed[i][j + 1]:
        data[i][j + 1] += 1
        if data[i][j + 1] == 10:
            flashing.append((i, j + 1))
    if i - 1 >= 0 and j + 1 < len(data[0]) and not flashed[i - 1][j + 1]:
        data[i - 1][j + 1] += 1
        if data[i - 1][j + 1] == 10:
            flashing.append((i - 1, j + 1))


if __name__ == "__main__":
    print(solve(load_input(day), 1))
    print(solve(load_input(day)))
