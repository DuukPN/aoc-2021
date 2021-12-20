from lib import load_input


def solve(data, part=2):
    lines = data.splitlines()
    code = lines[0]
    image = lines[2:]
    if part == 1:
        return part_one(code, image)
    elif part == 2:
        return part_two(code, image)


def part_one(code, image):
    return enhance(code, image, 2)


def part_two(code, image):
    return enhance(code, image, 50)


def print_image(image):
    for line in image:
        print(line)


def enhance(code, image, reps):
    for rep in range(reps):
        new_image = [[None] * (len(image[0]) + 2) for _ in range(len(image) + 2)]
        for x in range(-1, len(image) + 1):
            for y in range(-1, len(image[0]) + 1):
                num = ""
                for i in range(x - 1, x + 2):
                    for j in range(y - 1, y + 2):
                        if i in range(len(image)) and j in range(len(image[0])):
                            num += image[i][j]
                        else:
                            num += "#" if code[0] == "#" and rep % 2 else "."

                n = int(num.replace(".", "0").replace("#", "1"), 2)
                new_image[x + 1][y + 1] = code[n]

        image = new_image

    return sum(sum(c == "#" for c in line) for line in image)


if __name__ == "__main__":
    print(solve(load_input(""), 1))
    print(solve(load_input("")))
