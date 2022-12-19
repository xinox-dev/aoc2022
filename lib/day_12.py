# part 1
def count_steps_start_to_end(lines):
    dict_map, start, end = parse_map(lines)
    visited = set()
    visited.add(start)

    steps_start_to_end = 0

    while not end in visited:
        steps_start_to_end += 1
        visited = move_to_up(dict_map, visited)

    return steps_start_to_end


# part 2
def count_steps_in_faster_road(lines):
    dict_map, start, end = parse_map(lines)
    visited = set()
    visited.add(end)

    steps_in_faster_road = 0

    while True:
        steps_in_faster_road += 1
        visited = move_to_down(dict_map, visited)
        if check_low_height(visited, dict_map):
            break

    return steps_in_faster_road


def move_to_up(dict_map, visited):
    new_visited = set()

    for ceil in visited:
        height = dict_map[ceil]
        for (x, y) in ((+1, 0), (-1, 0), (0, +1), (0, -1)):
            x, y = ceil[0] + x, ceil[1] + y
            if dict_map.get((x, y)) is not None and dict_map[(x, y)] <= height + 1:
                new_visited.add((x, y))

    return new_visited


def move_to_down(dict_map, visited):
    new_visited = set()

    for ceil in visited:
        height = dict_map[ceil]
        for (x, y) in ((+1, 0), (-1, 0), (0, +1), (0, -1)):
            x, y = ceil[0] + x, ceil[1] + y
            if dict_map.get((x, y)) is not None and dict_map[(x, y)] >= height - 1:
                new_visited.add((x, y))

    return new_visited


def check_low_height(visited, dict_map):
    for ceil in visited:
        if dict_map[ceil] == 0:
            return True

    return False

def parse_map(lines):
    dict_map = dict()
    start, end = tuple(), tuple()
    for i, line in enumerate(lines):
        for j, x in enumerate(line):
            if x == 'S':
                dict_map[(i, j)] = 0
                start = (i, j)
            elif x == 'E':
                dict_map[(i, j)] = 25
                end = (i, j)
            else:
                dict_map[(i, j)] = ord(x) - 97

    return dict_map, start, end
