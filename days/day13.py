from lib import load_input


def solve(data, part=2):
    dots = [(int(t.split(",")[0]), int(t.split(",")[1])) for t in data.split("\n\n")[0].splitlines()]
    instructions = data.split("\n\n")[1].splitlines()
    if part == 1:
        return part_one(dots, instructions)
    elif part == 2:
        return part_two(dots, instructions)


def part_one(dots, instructions):
    fold = instructions[0].split(" ")[2].split("=")
    axis = 0 if fold[0] == "x" else 1
    value = int(fold[1])
    distinct = len(dots)
    for d in dots:
        if d[axis] > value:
            if axis:
                new_d = (d[0], 2 * value - d[1])
            else:
                new_d = (2 * value - d[0], d[1])
            if new_d in dots:
                distinct -= 1

    return distinct


def part_two(dots, instructions):
    for instr in instructions:
        fold = instr.split(" ")[2].split("=")
        axis = 0 if fold[0] == "x" else 1
        value = int(fold[1])

        new_dots = []

        for d in dots:
            if d[axis] > value:
                if axis:
                    new_d = (d[0], 2 * value - d[1])
                else:
                    new_d = (2 * value - d[0], d[1])
                if new_d not in dots:
                    new_dots.append(new_d)
            else:
                new_dots.append(d)

        dots = new_dots

    grid = ""
    for y in range(max(i for _, i in dots) + 1):
        curr_line = ""
        for x in range(max(i for i, _ in dots) + 1):
            curr_line += ("#" if (x, y) in dots else ".")
        grid += curr_line + "\n"

    return grid


if __name__ == "__main__":
    print(solve(load_input(), 1))
    print(solve(load_input()))
