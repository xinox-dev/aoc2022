def contains_pairs(pairs):
    counter = 0

    for pair in pairs:
        left, right = [tuple(int(n) for n in s.split("-")) for s in pair.split(',')]
        min_l, max_l = left
        min_r, max_r = right

        if (min_l <= min_r and max_l >= max_r) or (min_l >= min_r and max_l <= max_r):
            counter += 1

    return counter


def overlaps_pairs(pairs):
    counter = 0

    for pair in pairs:
        left, right = [tuple(int(n) for n in s.split("-")) for s in pair.split(',')]
        min_l, max_l = left
        min_r, max_r = right

        if (max_l >= min_r and min_l <= max_r) or (max_r >= min_l and min_r <= max_l):
            counter += 1

    return counter
