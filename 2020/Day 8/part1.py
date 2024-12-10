from utils.boot_code_machine import BootCodeMachine

data = [tuple([c for c in n.strip().split()]) for n in open("input.txt").readlines()]
# data = open("input.txt").read()
program = BootCodeMachine(data, 0)
print(program.accumulator)
