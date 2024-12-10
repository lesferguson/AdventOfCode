
rows = [r.strip() for r in open("input.txt").readlines()]
seat_ids = []
for row in rows:
    data = ''.join(['0' if i == "F" or i == "L" else '1' for i in row])
    row_n = int(data[:7], 2)
    seat_n = int(data[7:], 2)
    seat_ids.append(row_n * 8 + seat_n)

seat_ids.sort()


for i, id in enumerate(seat_ids):
    if i + 1 == len(seat_ids):
        break
    elif id + 1 == seat_ids[i+1]:
        continue
    elif id + 2 == seat_ids[i+1]:
        print(id + 1)
        print(int(id/8), id % 8)
    else:
        continue
# data = open("input.txt").read()
