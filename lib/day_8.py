def count_visible_trees(map_of_trees):
    ny = len(map_of_trees)
    nx = len(map_of_trees[0])
    counter = 2 * (ny-1) + 2 * (nx-1)   # add trees in outside

    for y in range(1, ny-1):
        for x in range(1, nx-1):
            size = map_of_trees[y][x]   # size of current tree
            # take max weight  of left, right, up, down
            max_l = max(map_of_trees[y][:x])
            max_r = max(map_of_trees[y][x+1:])
            max_u = max([row[x] for row in map_of_trees[0:y]])
            max_d = max([row[x] for row in map_of_trees[y+1:]])
            # if any direction has all smallest trees, tree is visible
            if size > min(max_l, max_r, max_u, max_d):
                counter += 1

    return counter


def highest_scenic_score(map_of_trees):
    ny = len(map_of_trees)
    nx = len(map_of_trees[0])
    best_sc = 0  # best scenic score

    for y in range(1, ny-1):
        for x in range(1, nx-1):
            size = map_of_trees[y][x]   # size of current tree
            # take trees of left, right, up, down
            lt = [_ for _ in map_of_trees[y][:x]][::-1]    # need reverse
            rt = [_ for _ in map_of_trees[y][x+1:]]
            ut = [row[x] for row in map_of_trees[0:y]][::-1]    # need reverse
            dt = [row[x] for row in map_of_trees[y+1:]]

            scenic_score = 1
            for trees in (lt, rt, ut, dt):
                c = 0   # counter of visible trees
                for t in trees:
                    if t < size:
                        c += 1
                    else:
                        c += 1
                        break

                scenic_score *= c

            best_sc = max(scenic_score, best_sc)

    return best_sc

