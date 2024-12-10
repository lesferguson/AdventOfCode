from copy import deepcopy

input_file = "input.txt"
# input_file = "test.txt"

data = [line.strip() for line in open(input_file).readlines()]
# data = [tuple([col for col in line.strip().split()]) for line in open(input_file).readlines()]
# data = open(input_file).read()
# data = [[val for val in line.strip().split(",")] for line in open(input_file).readlines()]
answers_sum = 0

for problem in data:
    problem_pieces = problem.split()
    print(problem)
    n = 0
    level = 0
    layers = {(0, 0): [], "max_depth": 0}
    current_layer = (0, 0)
    layer_start = [0]
    while n < len(problem_pieces):
        if "(" in problem_pieces[n]:
            first = True
            for layer in range(problem_pieces[n].count("(")):
                layer_start.append(n)
                level += 1
                layers[(layer_start[-1], level)] = []
                if layer == problem_pieces[n].count("(")-1:
                    layers[(layer_start[-1], level)].append(problem_pieces[n].lstrip("("))
                current_layer = (layer_start[-1], level)
                if layers["max_depth"] < level:
                    layers["max_depth"] = level

        elif ")" in problem_pieces[n]:
            for layer in range(problem_pieces[n].count(")")):
                if layer == 0:
                    layers[(layer_start[-1], level)].append(problem_pieces[n].rstrip(")"))

                prev_layer = current_layer
                layer_start.pop(-1)
                level -= 1
                current_layer = (layer_start[-1], level)
                layers[current_layer].append(prev_layer)
        else:
            layers[current_layer].append(problem_pieces[n])


        n += 1
    # print(layers)

    layers_new = layers.copy()
    for i in reversed(range(layers["max_depth"]+1)):
        for k in layers:
            if k == "max_depths":
                continue
            elif k[1] == i:
                ans = None

                for j, val in enumerate(layers[k]):
                    if type(val) is tuple:
                        layers[k][j] = layers[val]

                while "+" in layers[k]:
                    for j, val in enumerate(layers[k]):
                        if val == "+":
                            prod = int(layers[k][j-1]) + int(layers[k][j+1])
                            layers[k].pop(j+1)
                            layers[k].pop(j)
                            layers[k][j-1] = prod
                            # print(layers[k])

                ans = 1
                for j, val in enumerate(layers[k]):
                    if val != "*":
                        ans *= int(val)

                layers[k] = ans




                # for j, val in enumerate(layers[k]):
                #     if val in ["+", "*"]:
                #         continue
                #     if not ans:
                #         ans = int(val)
                #     else:
                #         if layers[k][j-1] == "*":
                #             ans *= int(val)
                #         elif layers[k][j-1] == "+":
                #             ans += int(val)
                layers[k] = ans
    print(layers[(0,0)])
    answers_sum += layers[(0, 0)]

print(answers_sum)

