instructions = None

path = {"wire1": [], "wire2":[]}

for wire, instruction in instructions.items():
    wire_path = (0, 0)
    for command in instruction:
        direction = command[0]
        distance = int(command[1:])

        for d in range(distance):
            if direction == "R":
                wire_path = (wire_path[0] + 1, wire_path[1])
            elif direction == "L":
                wire_path = (wire_path[0] - 1, wire_path[1])
            elif direction == "U":
                wire_path = (wire_path[0], wire_path[1] + 1)
            elif direction == "D":
                wire_path = (wire_path[0], wire_path[1] - 1)
            path[wire].append(wire_path)

connections = set(path["wire1"]).intersection(path["wire2"])
dis = 99999999999
for c in connections:
    wire1_distance = path["wire1"].index(c)+1
    wire2_distance = path["wire2"].index(c)+1
    cs = wire1_distance + wire2_distance
    if cs < dis:
        dis = cs
    print(cs)
print(dis)


