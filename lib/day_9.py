def rope_mark(series_of_motions):
    pos_head = [0, 0]   # (x, y)
    pos_tail = [0, 0]
    visited = set()
    for motion in series_of_motions:
        direction, steps = motion.split()
        for i in range(int(steps)):
            if direction == "R":
                pos_head[0] += 1
            elif direction == "L":
                pos_head[0] -= 1
            elif direction == "U":
                pos_head[1] += 1
            else:
                pos_head[1] -= 1

            pos_tail = move_rope_part(pos_head, pos_tail)
            visited.add(pos_tail)

    return len(visited)


def mark_of_large_rope(series_of_motions):
    rope = [[0, 0] for _ in range(10)]
    print(rope)
    visited = set()

    for motion in series_of_motions:
        direction, steps = motion.split()
        for i in range(int(steps)):
            if direction == "R":
                rope[0][0] += 1
            elif direction == "L":
                rope[0][0] -= 1
            elif direction == "U":
                rope[0][1] += 1
            else:
                rope[0][1] -= 1
            for i in range(9):
                rope[i+1] = list(move_rope_part(rope[i], rope[i+1]))

            visited.add(tuple(rope[-1]))

    return len(visited)


def move_rope_part(pos_head, pos_tail):
    xh, yh = pos_head
    xt, yt = pos_tail

    if xh == xt and yh == yt + 2:
        return xt, yt + 1
    elif xh == xt and yh == yt - 2:
        return xt, yt - 1
    elif yh == yt and xh == xt + 2:
        return xt + 1, yt
    elif yh == yt and xh == xt - 2:
        return xt - 1, yt
    elif (xh == xt + 2 and yh == yt + 1) or (xh == xt + 1 and yh == yt + 2) or (xh == xt + 2 and yh == yt + 2):
        return xt + 1, yt + 1
    elif (xh == xt + 2 and yh == yt - 1) or (xh == xt + 1 and yh == yt - 2) or (xh == xt + 2 and yh == yt - 2):
        return xt + 1, yt - 1
    elif (xh == xt - 2 and yh == yt - 1) or (xh == xt - 1 and yh == yt - 2) or (xh == xt - 2 and yh == yt - 2):
        return xt - 1, yt - 1
    elif (xh == xt - 2 and yh == yt + 1) or (xh == xt - 1 and yh == yt + 2) or (xh == xt - 2 and yh == yt + 2):
        return xt - 1, yt + 1
    else:
        return xt, yt


