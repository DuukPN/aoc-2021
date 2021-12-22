from lib import load_input


def solve(data, part=2):
    lines = data.splitlines()
    if part == 1:
        return part_one(lines)
    elif part == 2:
        return part_two(lines)


def part_one(data):
    on = set()
    for line in data:
        instr = line.split(" ")
        coords = instr[1].split(",")
        xs = [int(x) for x in coords[0][2:].split("..")]
        xs = range(max(min(xs), -50), min(max(xs), 50) + 1)
        ys = [int(y) for y in coords[1][2:].split("..")]
        ys = range(max(min(ys), -50), min(max(ys), 50) + 1)
        zs = [int(z) for z in coords[2][2:].split("..")]
        zs = range(max(min(zs), -50), min(max(zs), 50) + 1)

        curr_set = set()
        for x in xs:
            for y in ys:
                for z in zs:
                    if abs(x) <= 50 and abs(y) <= 50 and abs(z) <= 50:
                        curr_set.add((x, y, z))

        if instr[0] == "on":
            on |= curr_set
        else:
            on -= curr_set

    return len(on)


def part_two(data):
    pass


if __name__ == "__main__":
    print(solve(load_input(""), 1))
    print(solve(load_input("small")))
