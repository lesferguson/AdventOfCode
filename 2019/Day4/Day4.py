
possibles = []
for p in range(172851, 675869):
    if p == 667789:
        print("test")
    bad = False
    double = False
    p = str(p)
    for i in range(5):
        if p[i] > p[i+1]:
            bad = True
            break
    if bad:
        continue
    for i in range(5):
        if p[i] == p[i+1]:
            if (i != 4 and p[i] != p[i+2]) or i == 4:
                if (i > 1 and p[i] != p[i - 2]) or i <= 1:
                    if (0 < i <= 4 and (p[i] != p[i - 1] or p[i] != p[i + 1])) or i == 0:
                        double = True

    if not bad and double:
        possibles.append(p)
print(possibles)
print(len(possibles))
