

def run(data):

    o2 = data.copy()
    for i in range(len(o2[0])):
        if len(o2)==1:
            break
        ones = 0
        for j in range(len(o2)):
            if o2[j][i] == "1":
                ones += 1
        removals=[]
        if ones > len(o2) / 2:

            for n, row in enumerate(o2.copy()):
                if row[i]!="1":
                    removals.append(n)
        elif ones < len(o2) / 2:
            for n, row in enumerate(o2.copy()):
                if row[i] != "0":
                    removals.append(n)
        else:
            for n, row in enumerate(o2.copy()):
                if row[i]!="1":
                    removals.append(n)

        if not removals:
            print("test")
        removals.reverse()
        for r in removals:
            del(o2[r])


    co2 = data.copy()
    for i in range(len(co2[0])):
        if len(co2)==1:
            break
        ones = 0
        for j in range(len(co2)):
            if co2[j][i] == "1":
                ones += 1
        removals=[]
        if ones < len(co2) / 2:

            for n, row in enumerate(co2.copy()):
                if row[i]!="1":
                    removals.append(n)
        elif ones > len(co2) / 2:
            for n, row in enumerate(co2.copy()):
                if row[i] != "0":
                    removals.append(n)
        else:
            for n, row in enumerate(co2.copy()):
                if row[i]!="0":
                    removals.append(n)
        removals.reverse()
        for r in removals:
            del(co2[r])

    return int(''.join(o2[0]),2) * int(''.join(co2[0]),2)