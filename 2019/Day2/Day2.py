import sys

intcode_raw = None


for noun in range(99):
    for verb in range(99):
        i = 0
        intcode = intcode_raw.copy()
        intcode[1] = noun
        intcode[2] = verb
        while i <= len(intcode):
            code = intcode[i]
            if code == 99:
                if intcode[0] == 19690720:
                    print(f"noun:{noun} - verb:{verb} - output:{intcode[0]}")
                    sys.exit()
                else:
                    break

            elif code == 1:
                pos1 = intcode[i + 1]
                pos2 = intcode[i + 2]
                out = intcode[i + 3]
                intcode[out] = intcode[pos1] + intcode[pos2]
                i += 4
            elif code == 2:
                pos1 = intcode[i + 1]
                pos2 = intcode[i + 2]
                out = intcode[i + 3]
                intcode[out] = intcode[pos1] * intcode[pos2]
                i += 4
            else:
                print(f"{i} - {code}")
                break

