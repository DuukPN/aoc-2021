import re
from lib import load_input


def solve(data, part=2):
    lines = data.splitlines()
    nums = [int(x) for x in lines[0].split(",")]
    boards = []
    for i in range(2, len(lines), 6):
        board = []
        for j in range(i, i+5):
            board.append([int(x) for x in re.split("\\s+", lines[j].strip())])
        boards.append(board)

    if part == 1:
        return part_one(nums, boards)
    elif part == 2:
        return part_two(nums, boards)


def part_one(nums, boards):
    sums, last_numbers = play_bingo(nums, boards)

    ind = last_numbers.index(min(last_numbers))
    return sums[ind] * nums[last_numbers[ind]]


def part_two(nums, boards):
    sums, last_numbers = play_bingo(nums, boards)

    ind = last_numbers.index(max(last_numbers))
    return sums[ind] * nums[last_numbers[ind]]


def play_bingo(nums, boards):
    sums_of_unmarked = []
    index_of_last_number = []
    for board in boards:
        taken = [[False, False, False, False, False],
                 [False, False, False, False, False],
                 [False, False, False, False, False],
                 [False, False, False, False, False],
                 [False, False, False, False, False]]
        for n, num in enumerate(nums):
            for i in range(len(board)):
                for j in range(len(board[i])):
                    if board[i][j] == num:
                        taken[i][j] = True
            for k in range(len(board)):
                column = []
                for p in range(len(board)):
                    column.append(taken[p][k])
                if all(taken[k]) or all(column):
                    sum_of_unmarked = 0
                    for i in range(len(board)):
                        for j in range(len(board[i])):
                            if not taken[i][j]:
                                sum_of_unmarked += board[i][j]
                    sums_of_unmarked.append(sum_of_unmarked)
                    index_of_last_number.append(n)
                    break
            else:
                continue
            break

    return sums_of_unmarked, index_of_last_number


if __name__ == "__main__":
    print(solve(load_input(), 1))
    print(solve(load_input()))
