from heapq import heappush, heappop

from lib import load_input


def solve(data, part=2):
    lines = data.splitlines()
    if part == 1:
        return part_one(lines)
    elif part == 2:
        return part_two(lines)


def part_one(data):
    return dijkstra(data)


def part_two(data):
    rows = []
    for line in data:
        curr_row = ""
        for i in range(5):
            for c in line:
                new_digit = i + int(c)
                if new_digit > 9:
                    new_digit -= 9
                curr_row += (str(new_digit))
        rows.append(curr_row)

    total_data = []
    for i in range(5):
        for row in rows:
            curr_row = ""
            for c in row:
                new_digit = i + int(c)
                if new_digit > 9:
                    new_digit -= 9
                curr_row += (str(new_digit))
            total_data.append(curr_row)

    return dijkstra(total_data)


def dijkstra(data):
    pq = []
    visited = set()
    heappush(pq, (0, (0, 0)))
    while len(pq):
        curr = heappop(pq)
        coord = curr[1]
        if coord == (len(data) - 1, len(data[0]) - 1):
            return curr[0]
        if coord in visited:
            continue

        visited.add(coord)
        for edge in [(coord[0] - 1, coord[1]), (coord[0] + 1, coord[1]),
                     (coord[0], coord[1] - 1), (coord[0], coord[1] + 1)]:
            if edge[0] in range(len(data)) and edge[1] in range(len(data[0])) and edge not in visited:
                heappush(pq, (curr[0] + int(data[edge[0]][edge[1]]), edge))

    return -1


if __name__ == "__main__":
    print(solve(load_input(""), 1))
    print(solve(load_input("")))
