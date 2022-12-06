def start_of_packet_marker(packet):
    packet = packet[0]
    n = len(packet)
    for i in range(4, n):
        if len(set(packet[i - 4:i])) == 4:
            return i


def start_of_message_marker(packet):
    packet = packet[0]
    n = len(packet)
    for i in range(14, n):
        if len(set(packet[i - 14:i])) == 14:
            return i
