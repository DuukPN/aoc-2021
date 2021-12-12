from lib import load_input


def solve(data, part=2):
    lines = data.splitlines()
    if part == 1:
        return part_one(lines)
    elif part == 2:
        return part_two(lines)


def part_one(data):
    return sum([sum([1 if len(i) != 5 and len(i) != 6 else 0 for i in line]) for line in [line.split(" ") for line in [line.split(" | ")[1] for line in data]]])


def part_two(data):
    total = 0
    for line in data:
        code = [None] * 10
        values = [s for s in line.split(" | ")[0].split(" ")]

        fives = []
        sixes = []
        for v in values:
            if len(v) == 2:
                code[1] = v
            if len(v) == 3:
                code[7] = v
            if len(v) == 4:
                code[4] = v
            if len(v) == 5:
                fives.append(v)
            if len(v) == 6:
                sixes.append(v)
            if len(v) == 7:
                code[8] = v

        for s in sixes:
            if len([x for x in s if x in code[4]]) == 4:
                code[9] = s
            elif len([x for x in s if x in code[1]]) == 1:
                code[6] = s
            else:
                code[0] = s

        for f in fives:
            if len([x for x in f if x in code[9]]) == 4:
                code[2] = f
        for f in fives:
            common = len([x for x in f if x in code[2]])
            if common == 3:
                code[5] = f
            if common == 4:
                code[3] = f

        number = ""
        for n in line.split(" | ")[1].split(" "):
            for i, c in enumerate(code):
                if len(c) == len(n) and len([x for x in n if x in c]) == len(n):
                    number += str(i)

        total += int(number)

    return total


if __name__ == "__main__":
    print(solve(load_input(), 1))
    print(solve(load_input()))
