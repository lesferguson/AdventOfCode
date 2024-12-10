

def run(data):

    x = 1
    cycle = 0
    wait = 0
    cached_instruction = ()
    total_signal_strength = 0
    while data or cached_instruction:
        cycle += 1
        if (cycle + 20) % 40 == 0:
            # print(f"{cycle} * {x} = {x * cycle}")
            total_signal_strength += x * cycle
            if cycle == 220:
                break
        if wait > 1:
            wait -= 1
            continue
        if wait == 1:
            wait -= 1
            if cached_instruction[0] == "addx":
                x += int(cached_instruction[1])
            cached_instruction = ()
            continue




        instruction = data.pop(0)
        if instruction[0] == "noop":
            continue
        elif instruction[0] == "addx":
            wait = 1
            cached_instruction = instruction
            continue
        else:
            raise SyntaxError(f"Invalid operation in instructions: {instruction}")

    return total_signal_strength