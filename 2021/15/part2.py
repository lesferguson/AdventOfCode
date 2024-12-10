import math
import sys
from collections import deque


class Graph:
    def __init__(self, adjac_lis):
        self.adjac_lis = adjac_lis

    def get_neighbors(self, v):
        return self.adjac_lis[v]

    # This is heuristic function which is having equal values for all nodes
    def h(self, n):
        H = {
            'A': 1,
            'B': 1,
            'C': 1,
            'D': 1
        }

        return H[n]

    def a_star_algorithm(self, start, stop):
        # In this open_lst is a lisy of nodes which have been visited, but who's
        # neighbours haven't all been always inspected, It starts off with the start
        # node
        # And closed_lst is a list of nodes which have been visited
        # and who's neighbors have been always inspected
        open_lst = set([start])
        closed_lst = set([])

        # poo has present distances from start to all other nodes
        # the default value is +infinity
        poo = {}
        poo[start] = 0

        # par contains an adjac mapping of all nodes
        par = {}
        par[start] = start

        while len(open_lst) > 0:
            n = None

            # it will find a node with the lowest value of f() -
            for v in open_lst:
                if n == None or poo[v] + self.h(v) < poo[n] + self.h(n):
                    n = v;

            if n == None:
                print('Path does not exist!')
                return None

            # if the current node is the stop
            # then we start again from start
            if n == stop:
                reconst_path = []

                while par[n] != n:
                    reconst_path.append(n)
                    n = par[n]

                reconst_path.append(start)

                reconst_path.reverse()

                print('Path found: {}'.format(reconst_path))
                return reconst_path

            # for all the neighbors of the current node do
            for (m, weight) in self.get_neighbors(n):
                # if the current node is not presentin both open_lst and closed_lst
                # add it to open_lst and note n as it's par
                if m not in open_lst and m not in closed_lst:
                    open_lst.add(m)
                    par[m] = n
                    poo[m] = poo[n] + weight

                # otherwise, check if it's quicker to first visit n, then m
                # and if it is, update par data and poo data
                # and if the node was in the closed_lst, move it to open_lst
                else:
                    if poo[m] > poo[n] + weight:
                        poo[m] = poo[n] + weight
                        par[m] = n

                        if m in closed_lst:
                            closed_lst.remove(m)
                            open_lst.add(m)

            # remove n from the open_lst, and add it to closed_lst
            # because all of his neighbors were inspected
            open_lst.remove(n)
            closed_lst.add(n)

        print('Path does not exist!')
        return None

def run(data):
    side_size=int(math.sqrt(len(data)))
    big_data = {}
    risk_increase = lambda x: x + 1 if x < 9 else 1
    # Need to populate the remaing tiles
    for node, difficulty in data.items():
        big_data[node] = difficulty
        for i in range(1, 5):
            difficulty = risk_increase(difficulty)
            big_data[(node[0]+side_size*(i), node[1])] = difficulty
    old_data = big_data.copy()
    for node, difficulty in old_data.items():
        big_data[node] = difficulty
        for i in range(1, 5):
            difficulty = risk_increase(difficulty)
            big_data[(node[0], node[1]+side_size*(i))] = difficulty

    data = big_data
    side_size = int(math.sqrt(len(data)))

    nodes = []
    init_graph = {}
    for node in data:
        nodes.append(node)
        init_graph[node] = {}
        for x, y in [(node[0] + i, node[1] + j) for i in (0, 1) for j in (0, 1) if
                     (i != 0 or j != 0) and abs(i) != abs(j)]:
            if side_size > x >= 0 and side_size > y >= 0:
                init_graph[node][(x, y)] = data[(x, y)]
        init_graph[node] = [(k,v) for k,v in init_graph[node].items()]
    graph1 = Graph(init_graph)
    graph1.a_star_algorithm((0,0), (side_size-1,side_size-1))

    return
