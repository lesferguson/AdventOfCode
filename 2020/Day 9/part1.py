
data = [int(line.strip()) for line in open("input.txt").readlines()]
# data = open("input.txt").read()
print(data)
for n in range(25, len(data)):
    sub_list = data[n-25:n-0]
    possible_values = []
    for c, i in enumerate(sub_list):
        options = sub_list.copy()
        options.pop(c)
        for j in options:
            possible_values.append(i+j)
    if data[n] not in possible_values:
        print("bad", data[n], n)

