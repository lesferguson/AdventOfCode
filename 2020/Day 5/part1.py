
rows = [r.strip() for r in open("input.txt").readlines()]
seat_ids = []
for row in rows:
    data = ''.join(['0' if i == "F" or i == "L" else '1' for i in row])
    print(data)
    row_n = int(data[:7], 2)
    seat_n = int(data[7:], 2)
    seat_ids.append(row_n * 8 + seat_n)

print(max(seat_ids))
# data = open("input.txt").read()
