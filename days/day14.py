from collections import defaultdict
from lib import load_input


def solve(data, part=2):
    start = data.splitlines()[0]
    lines = {}
    for line in data.splitlines()[2:]:
        lines[line.split(" -> ")[0]] = line.split(" -> ")[1]
    if part == 1:
        return part_one(start, lines)
    elif part == 2:
        return part_two(start, lines)


def part_one(start, insertions):
    for _ in range(10):
        new_list = start[0]
        for i in range(1, len(start)):
            new_list += insertions[start[i-1] + start[i]] + start[i]
        start = new_list

    occurrences = defaultdict(int)
    for c in start:
        occurrences[c] += 1

    most_common = max(occurrences, key=occurrences.get)
    least_common = min(occurrences, key=occurrences.get)

    return occurrences[most_common] - occurrences[least_common]


def part_two(start, insertions):
    pairs = defaultdict(int)
    elements = defaultdict(int)
    elements[start[0]] += 1
    for i in range(1, len(start)):
        pairs[start[i-1] + start[i]] += 1
        elements[start[i]] += 1

    for _ in range(40):
        new_pairs = defaultdict(int)
        for k, v in pairs.items():
            c = insertions[k]
            new_pairs[k[0] + c] += v
            new_pairs[c + k[1]] += v
            elements[c] += v
        pairs = new_pairs

    most_common = max(elements, key=elements.get)
    least_common = min(elements, key=elements.get)

    return elements[most_common] - elements[least_common]


if __name__ == "__main__":
    print(solve(load_input(), 1))
    print(solve(load_input()))
