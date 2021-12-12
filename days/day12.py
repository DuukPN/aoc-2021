from lib import load_input
from collections import defaultdict


def solve(data, part=2):
    edges = defaultdict(list)
    for line in data.splitlines():
        a, b = line.split("-")
        edges[a].append(b)
        edges[b].append(a)
    if part == 1:
        return part_one(edges)
    elif part == 2:
        return part_two(edges)


def part_one(edges):
    return paths_recursive(edges, "start", defaultdict(int))


def part_two(edges):
    return paths_recursive(edges, "start", defaultdict(int), 2)


def paths_recursive(edges, curr, visited, threshold=1):
    if curr == "end":
        return 1
    if curr == "start" and visited["start"] == 1:
        return 0

    if curr.islower():
        visited[curr] += 1

    paths = 0
    for edge in edges[curr]:
        if not (threshold in visited.values() and visited[edge] >= 1):
            paths += paths_recursive(edges, edge, visited, threshold)

    if curr.islower():
        visited[curr] -= 1

    return paths


if __name__ == "__main__":
    print(solve(load_input(), 1))
    print(solve(load_input()))
