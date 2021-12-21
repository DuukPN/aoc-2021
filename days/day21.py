from collections import defaultdict

from lib import load_input


def solve(data, part=2):
    lines = [int(line.split(" ")[4]) for line in data.splitlines()]
    if part == 1:
        return part_one(*lines)
    elif part == 2:
        return part_two(*lines)


def part_one(p1, p2):
    p1 -= 1
    p2 -= 1
    s1 = 0
    s2 = 0
    die = 1
    while s1 < 1000 and s2 < 1000:
        p1 = (p1 + 3 * die + 3) % 10
        s1 += p1 + 1
        die += 3
        if s1 >= 1000:
            break
        p2 = (p2 + 3 * die + 3) % 10
        s2 += p2 + 1
        die += 3

    return (s1 if s1 < 1000 else s2) * (die - 1)


def part_two(p1, p2):
    universes = defaultdict(lambda: defaultdict(int))
    universes[(p1 - 1, p2 - 1)][(0, 0)] += 1
    wins = [0, 0]
    turn = 0
    roll = 0
    while len(universes.keys()) > 0:
        new_universes = defaultdict(lambda: defaultdict(int))
        roll += 1
        for key in universes.keys():
            for score in universes[key].keys():
                for i in range(3):
                    pos = list(key)
                    pos[turn] = (pos[turn] + i + 1) % 10
                    pos = tuple(pos)
                    new_score = score
                    if roll == 3:
                        new_score = list(score)
                        new_score[turn] += pos[turn] + 1
                        new_score = tuple(new_score)

                        if new_score[turn] >= 21:
                            wins[turn] += universes[key][score]
                            continue

                    new_universes[pos][new_score] += universes[key][score]

        universes = new_universes
        if roll == 3:
            turn = 1 - turn
            roll = 0

    return max(wins)


if __name__ == "__main__":
    print(solve(load_input(""), 1))
    print(solve(load_input("")))
