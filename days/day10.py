from lib import load_input

day = 10


def solve(data, part=2):
    lines = data.splitlines()
    if part == 1:
        return part_one(lines)
    elif part == 2:
        return part_two(lines)


def part_one(data):
    opening = ["(", "[", "{", "<"]
    closing = [")", "]", "}", ">"]
    error_points = {")": 3, "]": 57, "}": 1197, ">": 25137}
    total = 0
    stack = []
    for line in data:
        for c in line:
            if c in opening:
                stack.append(opening.index(c))
            elif c in closing:
                if c != closing[stack.pop()]:
                    total += error_points[c]
                    break
        stack = []

    return total


def part_two(data):
    opening = ["(", "[", "{", "<"]
    closing = [")", "]", "}", ">"]
    totals = []
    stack = []
    for line in data:
        for c in line:
            if c in opening:
                stack.append(opening.index(c))
            elif c in closing:
                if c != closing[stack.pop()]:
                    break
        else:
            subtotal = 0
            while len(stack) > 0:
                subtotal *= 5
                subtotal += stack.pop() + 1
            totals.append(subtotal)
        stack = []

    totals.sort()

    return totals[len(totals) // 2]


if __name__ == "__main__":
    print(solve(load_input(day), 1))
    print(solve(load_input(day)))
