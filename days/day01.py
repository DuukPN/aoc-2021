from lib import load_input


def solve(data, part=2):
    nums = [int(line) for line in data.splitlines()]
    if part == 1:
        return part_one(nums)
    elif part == 2:
        return part_two(nums)


def part_one(data):
    return sum([data[i] > data[i - 1] for i in range(1, len(data))])


def part_two(data):
    return sum([data[i] > data[i - 3] for i in range(3, len(data))])


if __name__ == "__main__":
    print(solve(load_input(), 1))
    print(solve(load_input()))
