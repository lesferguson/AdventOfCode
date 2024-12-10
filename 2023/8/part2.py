import math

def run(data):
    steps = 0
    directions = data.pop(0)
    data.pop(0)
    rl_map = {"L": 0, "R": 1}
    network = {}
    for node in data:
        node_name, connections = node.split(" = ")
        connections = tuple(connections.strip("()").split(", "))
        network[node_name] = connections
        # print(node_name, connections)
    start_nodes = [node for node in network if node.endswith("A")]
    start_distance = {}
    for node in start_nodes:
        current_node = node
        distance = 0
        while not current_node.endswith("Z"):
            current_i = distance % len(directions)
            current_node = network[current_node][rl_map[directions[current_i]]]
            distance += 1
        start_distance[node] = distance
    print(start_distance)

    return math.lcm(*list(start_distance.values()))
