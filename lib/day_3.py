import string
from collections import Counter


def sum_priorities_of_rs(rucksacks):
    letters = [*string.ascii_letters]
    sum_of_priorities = 0

    for rucksack in rucksacks:
        n = len(rucksack)
        left_rs, right_rs = (rucksack[0:n//2], rucksack[n//2:])
        common_item = list(set(left_rs).intersection(right_rs))[0]
        sum_of_priorities += letters.index(common_item) + 1

    return sum_of_priorities


def sum_values_of_badges(rucksacks):
    letters = [*string.ascii_letters]
    values_of_badges = 0
    n = len(rucksacks)

    for i in range(0, n, 3):
        items_of_group = []
        for rucksack in rucksacks[i:i+3]:
            items_of_group.extend(set(rucksack))

        counter_items = Counter(items_of_group)
        common_item = counter_items.most_common(1)[0][0]    # get key from dict of most common item
        values_of_badges += letters.index(common_item) + 1

    return values_of_badges
