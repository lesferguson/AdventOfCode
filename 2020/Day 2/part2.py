
data = [((line.split(":")[0].strip().split(" ")[0], line.split(":")[0].strip().split(" ")[1]), line.split(":")[1].strip()) for line in open("input.txt").readlines()]
# data = open("input.txt").read()
valid_count = 0
for line in data:
    req_num = tuple(map(int, line[0][0].split("-")))
    req_letter = line[0][1]
    password = line[1]
    if password[req_num[0]-1] == req_letter and not password[req_num[1]-1] == req_letter:
        valid_count += 1
        # print(req_num, req_letter, password)
    elif not password[req_num[0]-1] == req_letter and password[req_num[1]-1] == req_letter:
        # print(req_num, req_letter, password)
        valid_count += 1
print(valid_count)
