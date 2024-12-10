import time
data = [int(line.strip()) for line in open("input.txt").readlines()]
# data = open("input.txt").read()
preamble_len = 25
for n in range(preamble_len, len(data)):
    sub_list = data[n-preamble_len:n-0]
    possible_values = []
    for c, i in enumerate(sub_list):
        options = sub_list.copy()
        options.pop(c)
        for j in options:
            possible_values.append(i+j)
    if data[n] not in possible_values:
        bad_index = n
        bad_value = data[n]



trunc_data = data[:bad_index]

start_loop = time.perf_counter()
for n in range(len(trunc_data)):
    summation = trunc_data[n]
    i = n
    while summation < bad_value:
        i += 1
        summation += trunc_data[i]
    if summation == bad_value:
        break

print(min(trunc_data[n:i+1])+max(trunc_data[n:i+1]))
end_loop = time.perf_counter()
print(end_loop-start_loop)

start_loop = time.perf_counter()
summation = trunc_data[0]
n = 0
cont_list = [trunc_data[0]]
while summation != bad_value:
    n += 1
    cont_list.append(trunc_data[n])
    summation = sum(cont_list)
    if summation < bad_value:
        continue
    elif summation > bad_value:
        while summation > bad_value:
            cont_list = cont_list[1:]
            summation = sum(cont_list)
    else:
        continue


print(min(cont_list)+max(cont_list))

end_loop = time.perf_counter()
print(end_loop-start_loop)