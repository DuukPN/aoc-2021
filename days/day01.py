from io import read_input


def solve(input):
    # return part_one(input)
    return part_two(input)


def part_one(input):
    increases = 0
    for i in range(1, len(input)):
        if input[i-1] < input[i]:
            increases += 1
    return increases


def part_two(input):
    increases = 0
    for i in range(3, len(input)):
        if input[i-3] < input[i]:
            increases += 1
    return increases


if __name__ == "__main__":
    print(solve(read_input("day01.txt")))
