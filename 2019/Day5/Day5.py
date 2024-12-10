import sys

intcode = None
i = 0
while i <= len(intcode):
    code = str(intcode[i])
    code = (5 - len(code)) * "0" + code
    vals = {}
    for n in range(3, 6):
        if code[-n] == "1":
            vals[n-2] = intcode[i + n-2]
        else:
            try:
                vals[n-2] = intcode[intcode[i + n-2]]
            except:
                pass

    if code.endswith("99"):
        break
    elif code.endswith("01"):
        out = intcode[i + 3]
        intcode[out] = vals[1] + vals[2]
        i += 4
    elif code.endswith("02"):
        out = intcode[i + 3]
        intcode[out] = vals[1] * vals[2]
        i += 4
    elif code.endswith("03"):
        s = input("Enter system ID:")
        intcode[intcode[i + 1]] = int(s)
        i += 2
    elif code.endswith("04"):
        print(vals[1])
        i += 2
    elif code.endswith("05"):
        target = vals[1]
        if target != 0:
            i = vals[2]
        else:
            i += 3
    elif code.endswith("06"):
        target = vals[1]
        if target == 0:
            i = vals[2]
        else:
            i += 3
    elif code.endswith("07"):
        if vals[1] < vals[2]:
            intcode[intcode[i+3]] = 1
        else:
            intcode[intcode[i + 3]] = 0
        i += 4
    elif code.endswith("08"):
        if vals[1] == vals[2]:
            intcode[intcode[i + 3]] = 1
        else:
            intcode[intcode[i + 3]] = 0
        i += 4
    else:
        print(f"{i} - {code}")
        sys.exit(1)
