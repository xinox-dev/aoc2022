def sum_of_signal_strengths(signals):
    cycle = 0
    power = 1
    signals_strengths = 0
    calc_signals = set()

    for signal in signals:
        if signal == 'noop':
            cycle += 1
        else:
            cycle += 2
            value = signal.split()[1]
            power += int(value)

        if cycle <= 220:
            if (cycle + 20) % 40 == 0:
                if not cycle in calc_signals:
                    print(cycle * (power - int(signal.split()[1])), 0, cycle, power)
                    signals_strengths += cycle * (power - int(signal.split()[1]))
                    calc_signals.add(cycle)
            elif (cycle + 21) % 40 == 0:
                print((cycle + 1) * power, 1)
                signals_strengths += power * (cycle + 1)
                calc_signals.add(cycle+1)

    return signals_strengths


def set_screen(signals):
    cycle = 0
    power = 1
    pixels = []

    for signal in signals:
        if signal == 'noop':
            pixels.append(add_pixel(cycle, power))
            cycle += 1
        else:
            for _ in range(2):
                pixels.append(add_pixel(cycle, power))
                cycle += 1

            value = signal.split()[1]
            power += int(value)

    return pixels


def add_pixel(cycle, power):
    pos_in_row = cycle % 40

    if power - 1 <= pos_in_row <= power + 1:
        return True
    else:
        return False


def draw_screen(signals):
    settings = set_screen(signals)

    for i, s in enumerate(settings):
        if i % 40 == 0:
            print('', end="\n")

        if s:
            print('#', sep='', end='')
        else:
            print('.', sep='', end='')







