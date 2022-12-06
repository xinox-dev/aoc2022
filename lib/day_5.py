def move_stack_of_crates(report_of_crates):
    settings = []
    start_logs = 0
    for log in report_of_crates:
        start_logs += 1
        if log == '':
            break
        else:
            settings.append(log)

    slots = load_stack(settings)

    for move in report_of_crates[start_logs:]:
        count, move = move.strip('move').split('from')
        from_, to = int(move[1]), int(move[-1])
        crate_mover_handle = []

        for i in range(int(count)):
            crate_mover_handle.append(slots[from_-1].pop())

        crate_mover_handle.reverse()
        slots[to-1].extend(crate_mover_handle)

    return ''.join(stack[-1] for stack in slots)


def load_stack(settings):
    n = (len(settings[-1]) + 2) // 4  # count len of slots
    slots = [[] for _ in range(n)]  # create empty slots
    for s in settings[:-1]:
        for i in range(0, n):
            if not s[i*4:i*4+3] == '' and not s[i*4:i*4+3] == '   ':
                slots[i].append(s[i*4+1])

    for stack in slots:
        stack.reverse()

    return slots