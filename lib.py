import os


def read_input(day):
    path = f"{os.path.dirname(os.getcwd())}/input/day{str(day).zfill(2)}.txt"
    f = open(path)
    data = []
    for line in f:
        data.append(line)
    return data
