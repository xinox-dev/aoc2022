def count_score_of_first_strategy(rounds):
    total_score = 0
    points_table = {
        "A": {"X": 4, "Y": 8, "Z": 3},
        "B": {"X": 1, "Y": 5, "Z": 9},
        "C": {"X": 7, "Y": 2, "Z": 6}
    }
    for r in rounds:
        opponent, me = r.split()
        total_score += points_table[opponent][me]

    return total_score


def count_score_of_second_strategy(rounds):
    total_score = 0
    points_table = {
        "X": {"A": 3, "B": 1, "C": 2},
        "Y": {"A": 4, "B": 5, "C": 6},
        "Z": {"A": 8, "B": 9, "C": 7}
    }
    for r in rounds:
        opponent, me = r.split()
        total_score += points_table[me][opponent]

    return total_score

