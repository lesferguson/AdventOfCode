from utils.boot_code_machine import BootCodeMachine


data = [tuple([c for c in n.strip().split()]) for n in open("input.txt").readlines()]
# data = open("input.txt").read()
for n, command in enumerate(data):
    mod_data = data.copy()
    if command[0] == "jmp":
        mod_data[n] = ("nop", command[1])
    elif command[0] == "nop":
        mod_data[n] = ("jmp", command[1])
    program = BootCodeMachine(mod_data, 0)
    if not program.error:
        print("Success:", program.accumulator)
        print(n, command)
        break
