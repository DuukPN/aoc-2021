from lib import read_input


def solve(data):
    # return part_one(input)
    return part_two(data)


def part_one(data):
    return sum([1 if data[i] > data[i - 1] else 0 for i in range(1, len(data))])


def part_two(data):
    return sum([1 if data[i] > data[i - 3] else 0 for i in range(3, len(data))])


if __name__ == "__main__":
    print(solve(read_input(1)))
