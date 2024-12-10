

def run(data):
    result = 0
    steps = 0
    directions = data.pop(0)
    data.pop(0)
    current_node = "AAA"
    rl_map = {"L":0, "R": 1}
    network = {}
    for node in data:
        node_name, connections = node.split(" = ")
        connections = tuple(connections.strip("()").split(", "))
        network[node_name] = connections
        # print(node_name, connections)
    while current_node != "ZZZ":
        current_i = steps%len(directions)
        current_node = network[current_node][rl_map[directions[current_i]]]
        steps += 1
    # print(network)


    return steps
