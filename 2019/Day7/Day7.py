from itertools import permutations
from intcode import intcode
from collections import deque
from operator import itemgetter
program = [int(option) for option in open("Day7input.txt", "r").read().split(",")]

phases = set(range(5, 10))
possible_phases = list(permutations(phases))
outputs = {}

for phase_list in possible_phases:
    signal = 0
    signal_o = 0
    computers = {}

    for phase in phase_list:
        computers[phase] = intcode(program.copy())
        signal = computers[phase].loop(deque([phase, signal]))
    while True:
        print(signal)
        for phase in phase_list:
            signal_o = computers[phase].loop(deque([signal]))
            if type(signal_o) == str:
                break
            else:
                signal = signal_o
        if type(signal_o) == str:
            break

    for phase in phase_list:
        del computers[phase]


    outputs[phase_list] = signal

m = max(outputs.items(), key=itemgetter(1))[0]

print(m, outputs[m])
pass