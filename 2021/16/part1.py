from collections import defaultdict, deque

def packet_parse(bits):
    global packet_version_sum
    packet_version = int(bits.popleft() + bits.popleft() + bits.popleft(), 2)
    packet_type = int(bits.popleft() + bits.popleft() + bits.popleft(), 2)
    packet_version_sum += packet_version

    if packet_type == 4:  # literal
        value = ""
        while True:
            value_chain_continued = bits.popleft()
            value_chunk = bits.popleft() + bits.popleft() + bits.popleft() + bits.popleft()
            value += value_chunk
            if value_chain_continued == "0":
                return value
    else:
        results = []
        subpacket_length = ""
        if bits.popleft() == "1":
            subpacket_count =""
            sub_count_length = 11
            for _ in range(sub_count_length):
                subpacket_count += bits.popleft()
            subpacket_count = int(subpacket_count, 2)
            for _ in range(subpacket_count):
                results.append(packet_parse(bits))
        else:
            subpacket_length = ""
            sub_count_length = 15
            for _ in range(sub_count_length):
                subpacket_length += bits.popleft()
            subpacket_length = int(subpacket_length, 2)

            start_len = len(bits)
            while start_len - len(bits) < subpacket_length:

                results.append(packet_parse(bits))
        return results


def run(data):

    bits = deque(list(format(int(data, 16), f"0>{len(data)*4}b")))

    global packet_version_sum
    packet_version_sum = 0

    results = packet_parse(bits)



    print("test")


    return results
