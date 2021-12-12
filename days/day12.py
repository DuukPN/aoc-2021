from collections import defaultdict

from lib import load_input

day = 12


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
    return len(paths_recursive(edges, "start", defaultdict(int)))


def part_two(edges):
    visited = defaultdict(int)
    paths = paths_recursive(edges, "start", visited, 2)
    return len(paths)


def paths_recursive(edges, curr, visited, threshold=1):
    if curr == "end":
        return [curr]
    if curr == "start" and visited["start"] == 1:
        return []

    res = []
    if curr.islower():
        visited[curr] += 1

    for edge in edges[curr]:
        if threshold in visited.values() and visited[edge] >= 1:
            continue
        paths = paths_recursive(edges, edge, visited, threshold)
        for path in paths:
            res.append(curr + "," + path)

    if curr.islower():
        visited[curr] -= 1

    return res


if __name__ == "__main__":
    print(solve(load_input(day), 1))
    print(solve(load_input(day)))
