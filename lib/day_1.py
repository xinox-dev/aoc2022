def calorie_counter(input):
    cal_of_elfs = [0, 0, 0]
    cal = 0

    for i in input:
        if i.isdigit():
            cal += int(i)
        else:
            cal_of_elfs.append(cal)
            cal_of_elfs = sorted(cal_of_elfs, reverse=True)[0:3]
            cal = 0
    # return top 3 elfs' calories of foods
    return sum(cal_of_elfs)
