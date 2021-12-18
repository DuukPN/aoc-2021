from lib import load_input


def solve(data, part=2):
    lines = []
    for line in data.splitlines():
        curr = []
        for c in line:
            if c in "[]":
                curr.append(c)
            elif c.isdigit():
                curr.append(int(c))
        lines.append(curr)

    if part == 1:
        return part_one(lines)
    elif part == 2:
        return part_two(lines)


def part_one(data):
    curr = []
    for line in data:
        if not curr:
            curr = line
            continue

        curr = add_numbers(curr, line)

    return magnitude(curr)


def part_two(data):
    largest = 0
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            one = magnitude(add_numbers(data[i], data[j]))
            if one > largest:
                largest = one

            two = magnitude(add_numbers(data[j], data[i]))
            if two > largest:
                largest = two

    return largest


def add_numbers(one, two):
    curr = ["[", *one, *two, "]"]

    while True:
        depth = 0
        for i, c in enumerate(curr):
            if c == "[":
                depth += 1
            elif c == "]":
                depth -= 1

            if depth == 5:
                left = curr[i + 1]
                j = i
                while j >= 0 and isinstance(curr[j], str):
                    j -= 1
                if j >= 0:
                    curr[j] += left

                right = curr[i + 2]
                j = i + 3
                while j < len(curr) and isinstance(curr[j], str):
                    j += 1
                if j < len(curr):
                    curr[j] += right

                curr[i:i + 4] = [0]

                break

        else:
            for i, c in enumerate(curr):
                if isinstance(c, int) and c >= 10:
                    n = int(c)
                    new = ["[", n // 2, n - n // 2, "]"]
                    curr[i:i + 1] = new

                    break

            else:
                break

    return curr


def magnitude(curr):
    while len(curr) > 1:
        for i, c in enumerate(curr):
            if isinstance(c, int) and isinstance(curr[i + 1], int):
                curr[i - 1:i + 3] = [3 * c + 2 * curr[i + 1]]
                break

    return curr[0]


if __name__ == "__main__":
    print(solve(load_input(""), 1))
    print(solve(load_input("")))
