from functools import reduce

from lib import load_input


def solve(data, part=2):
    binary_strings = ["".join(bin(int(c, 16))[2:].zfill(4) for c in line) for line in data.splitlines()]
    if len(binary_strings) == 1:
        if part == 1:
            return part_one(*binary_strings)
        elif part == 2:
            return part_two(*binary_strings)
    else:
        if part == 1:
            return [part_one(binary_string) for binary_string in binary_strings]
        elif part == 2:
            return [part_two(binary_string) for binary_string in binary_strings]


def part_one(data):
    return version_sum(data, 0)[0]


def part_two(data):
    return evaluate(data, 0)[0]


def version_sum(data, p):
    version = int(data[p:p + 3], 2)
    type_id = int(data[p + 3:p + 6], 2)
    if type_id == 4:
        ptr = p + 6
        number = data[ptr:ptr + 5]
        while number[0] == "1":
            ptr += 5
            number = data[ptr:ptr + 5]

        return version, ptr + 5

    length_type = int(data[p + 6:p + 7])
    if length_type:
        length = int(data[p + 7:p + 18], 2)
        ptr = p + 18
        for i in range(length):
            v, ptr = version_sum(data, ptr)
            version += v
    else:
        length = int(data[p + 7:p + 22], 2)
        ptr = p + 22
        while p + 22 + length > ptr:
            v, ptr = version_sum(data, ptr)
            version += v

    return version, ptr


def evaluate(data, p):
    type_id = int(data[p + 3:p + 6], 2)
    if type_id == 4:
        ptr = p + 6
        curr = data[ptr:ptr + 5]
        n = int(curr[1:], 2)
        while curr[0] == "1":
            n *= 16
            ptr += 5
            curr = data[ptr:ptr + 5]
            n += int(curr[1:], 2)

        return n, ptr + 5

    length_type = int(data[p + 6:p + 7])
    if length_type:
        length = int(data[p + 7:p + 18], 2)
        ptr = p + 18
        values = []
        for i in range(length):
            v, ptr = evaluate(data, ptr)
            values.append(v)
    else:
        length = int(data[p + 7:p + 22], 2)
        ptr = p + 22
        values = []
        while p + 22 + length > ptr:
            v, ptr = evaluate(data, ptr)
            values.append(v)

    if type_id == 0:
        n = sum(values)
    elif type_id == 1:
        n = reduce(lambda a, b: a * b, values)
    elif type_id == 2:
        n = min(values)
    elif type_id == 3:
        n = max(values)
    elif type_id == 5:
        n = values[0] > values[1]
    elif type_id == 6:
        n = values[0] < values[1]
    else:
        n = values[0] == values[1]

    return n, ptr


if __name__ == "__main__":
    print(solve(load_input(), 1))
    print(solve(load_input()))
