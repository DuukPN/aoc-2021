from lib import load_input

day = 3


def solve(data, part=2):
    lines = data.splitlines()
    if part == 1:
        return part_one(lines)
    elif part == 2:
        return part_two(lines)


def part_one(data):
    ones = []
    for i in range(len(data[0])):
        ones.append(0)
    for line in data:
        i = 0
        for c in line:
            if c == "1":
                ones[i] += 1
            i += 1
    gamma = ""
    epsilon = ""
    for f in ones:
        if f > len(data) / 2:
            gamma += "1"
            epsilon += "0"
        else:
            gamma += "0"
            epsilon += "1"
    return int(gamma, 2) * int(epsilon, 2)


def part_two(data):
    l = []
    for i in range(2):
        curr = ""
        for p in range(len(data[0])):
            size = 0
            freq = 0
            for line in data:
                if line.startswith(curr):
                    if line[p] == "1":
                        freq += 1
                    size += 1
            if size == 1:
                break
            if freq < size / 2:
                curr += str(i)
            else:
                curr += str(1-i)
        if len(curr) < len(data[0]):
            for line in data:
                if line.startswith(curr):
                    curr = line
                    break
        print(curr)
        l.append(int(curr, 2))
    return l[0] * l[1]


if __name__ == "__main__":
    print(solve(load_input(day), 1))
    print(solve(load_input(day)))
