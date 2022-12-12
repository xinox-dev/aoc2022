from copy import copy

def parse_monkeys(text):
    monkeys = []
    n = (len(text) + 1) / 7

    for i in range(0, (len(text) + 1), 7):
        items = list(map(int, text[i + 1].strip('Starting items: ').split(',')))
        value, symbol = text[i + 2].split()[:3:-1]
        symbol = 1 if symbol == '*' else 0
        value = int(value) if value.isdigit() else 0
        divisible = text[i + 3].split()[-1]
        t_true = text[i + 4].split()[-1]
        t_false = text[i + 5].split()[-1]

        monkey = [symbol, value, int(divisible), int(t_true), int(t_false)]
        monkey.extend(items)
        monkeys.append(monkey)

    return monkeys


def s(text):
    monkeys = parse_monkeys(text)
    counter_inspected_items = [0 for _ in range(len(monkeys))]
    supermodulo = (2*3*5*7*11*13*17*19*23)

    for _ in range(10000):
        for j, monkey in enumerate(monkeys):
            o_symbol = monkey[0]
            o_value = monkey[1]
            divisible = monkey[2]
            t_true = monkey[3]
            t_false = monkey[4]
            items = monkey[5:]

            for i, item in enumerate(items):
                worry_level = copy(item)

                if o_symbol:
                    if o_value == 0:
                        worry_level = worry_level * worry_level
                    else:
                        worry_level = worry_level * o_value

                else:
                    if o_value == 0:
                        worry_level = worry_level + worry_level
                    else:
                        worry_level = worry_level + o_value

                worry_level = worry_level % supermodulo

                if worry_level % divisible == 0:
                    monkeys[t_true].append(worry_level)
                else:
                    monkeys[t_false].append(worry_level)

                monkey.pop()
                counter_inspected_items[j] += 1

    counter_inspected_items.sort(reverse=True)

    return counter_inspected_items[0] * counter_inspected_items[1]