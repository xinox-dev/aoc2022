from collections import defaultdict


def drop_sand(cave: defaultdict):
    x, y = 500, 0  # start point for drop sand
    while y < 200:
        if cave[(x, y + 1)] is None:
            y += 1

        else:
            if cave[(x - 1, y + 1)] is None:
                x -= 1
                y += 1

            elif cave[(x + 1, y + 1)] is None:
                x += 1
                y += 1

            else:
                return x, y

    return x, y


def parse_cave(lines: list, is_floor: bool=False) -> dict:
    cave = defaultdict(lambda: None)
    floor, min_x, max_x = 0, 999, 0
    for line in lines:
        pivot_points = line.split(' -> ')
        n = len(pivot_points)

        for i in range(n - 1):
            x1, y1 = map(int, pivot_points[i].split(','))
            x2, y2 = map(int, pivot_points[i + 1].split(','))
            floor = max(floor, y1, y2)
            min_x = min(min_x, x1, x2)
            max_x = max(max_x, x1, x2)
            if x1 == x2:
                if y1 > y2:
                    for j in range(y2, y1 + 1):
                        cave[(x1, j)] = True
                else:
                    for j in range(y1, y2 + 1):
                        cave[(x1, j)] = True

            else:
                if x1 > x2:
                    for j in range(x2, x1 + 1):
                        cave[(j, y2)] = True
                else:
                    for j in range(x1, x2 + 1):
                        cave[(j, y1)] = True
    if is_floor:
        floor += 2
        for j in range(499 - floor, 501 + floor):
            cave[(j, floor)] = True

    return cave


def part1(input):
    cave = parse_cave(input)
    c = 0

    while True:
        x, y = drop_sand(cave)

        if y == 200:
            return c

        cave[(x, y)] = True
        c += 1


def part2(input):
    cave = parse_cave(input, is_floor=True)
    c = 0

    while True:
        x, y = drop_sand(cave)

        if x == 500 and y == 0:
            return c + 1

        cave[(x, y)] = True
        c += 1
