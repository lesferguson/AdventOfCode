from copy import deepcopy

import numpy
input_file = "input.txt"
# input_file = "test.txt"

# data = [int(line.strip()) for line in open(input_file).readlines()]
# data = [tuple([col for col in line.strip().split()]) for line in open(input_file).readlines()]
# data = open(input_file).read()

timestamp, buses = open(input_file).readlines()
timestamp, buses = int(timestamp), [(i, int(bus)) for i, bus in enumerate(buses.split(',')) if bus != 'x']
#
# first_bus = buses[0][0]
#
# buses = set(buses)
# print(first_bus)
# if ("x", None) in buses:
#     buses.remove(("x", None))
# buses = dict(buses)
# bus_ids = list(buses.keys())
# bus_ids.sort()
#
# for bus, remainder in buses.items():
#     print("x =", remainder, "mod", bus)
#
#
# departures = {}
# a = numpy.zeros((len(buses), len(buses)), dtype=int)
# b = numpy.full(len(buses), first_bus*1000000000000)
# for n, bus in enumerate(bus_ids):
#     a[n, n] = bus
#     b[n] += buses[bus]
#     if bus == first_bus:
#         solution_value = (bus, n)


# solution = numpy.full(1, .5)
#
# while not numpy.all([i.is_integer() for i in solution]):
#     b += first_bus
#     solution = numpy.linalg.solve(a, b)
#     # print(solution)
#     # if numpy.all([i.is_integer() for i in solution])
#
#
# print(a)
# print(solution_value)
# print(solution[solution_value[1]]*solution_value[0])
#
#
# def lcm(a: int, b: int):
#     return abs(a*b) // math.gcd(a, b)
#
#
# def solve_two(data: str):
#     buss_id_offsets: List[Tuple[int, int]] = [
#         (i, bid)
#         for i, bid in enumerate(parse_input(data)[1])
#         if bid != 'x'
#     ]
#
#     timestamp = 0
#     step = buss_id_offsets[0][1]
#     remaining = len(buss_id_offsets)
#     while remaining:
#         minutes, bid = buss_id_offsets[remaining - len(buss_id_offsets)]
#         if (timestamp + minutes) % bid == 0:
#             step = lcm(step, bid)
#             remaining -= 1
#         else:
#             timestamp += step
#
#     return timestamp
#


from functools import reduce

def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1

def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod

def part2(buses):
    dividers = [bus for _, bus in buses]
    remainders = [bus - i for i, bus in buses]
    for n in range(len(dividers)):
        print(remainders[n], dividers[n])
    return chinese_remainder(dividers, remainders)

print(part2(buses))