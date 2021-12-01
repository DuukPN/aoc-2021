from lib import read_input


def solve(input):
    # return part_one(input)
    return part_two(input)


def part_one(input):
    return sum([1 if input[i] > input[i - 1] else 0 for i in range(1, len(input))])


def part_two(input):
    return sum([1 if input[i] > input[i - 3] else 0 for i in range(3, len(input))])


if __name__ == "__main__":
    print(solve(read_input(1)))
