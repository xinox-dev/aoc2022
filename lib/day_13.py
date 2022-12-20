from itertools import zip_longest


def count_right_packets(lines):
    n = len(lines)
    one_packs, two_packs = 0, 0
    part1 = 0

    for i in range(0, n, 3):
        first_line = parse_list(lines[i], 0)[0]
        second_line = parse_list(lines[i+1], 0)[0]
        if check_list(first_line, second_line):
            part1 += (i//3) + 1

        for line in (first_line, second_line):
            if check_list(line, [[6]]):
                if check_list(line, [[2]]):
                    one_packs += 1
                else:
                    two_packs += 1

    part2 = (one_packs + 1) * (one_packs + two_packs + 2)

    return part2


def parse_list(s, i):
    l = []
    ten_flag = False
    while i < len(s):
        i += 1

        if ten_flag:
            ten_flag = False
            continue
        if s[i] == '[':
            li, i = parse_list(s, i)
            l.append(li)

        elif s[i] == '1':
            if i < (len(s) - 1) and s[i + 1] == '0':
                l.append(10)
                ten_flag = True
            else:
                l.append(1)

        elif s[i] == ']':
            return l, i

        elif s[i].isdigit():
            l.append(int(s[i]))


def check_list(l1, l2):
    for v1, v2 in zip_longest(l1, l2):
        res = None
        if v1 is None:
            return True

        elif v2 is None:
            return False

        type1, type2 = type(v1), type(v2)

        if type1 is list and type2 is list:
            res =  check_list(v1, v2)

        elif type1 is int and type2 is int:
            if v1 > v2:
                return False
            elif v2 > v1:
                return True

        elif type1 is int and type2 is list:
            res = check_list([v1], v2)

        elif type1 is list and type2 is int:
            res = check_list(v1, [v2])

        if not res is None:
            return res

