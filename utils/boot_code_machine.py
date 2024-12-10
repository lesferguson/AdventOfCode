class BootCodeMachine:
    def __init__(self, prog, start_index=0):
        self.program = prog
        self.index = start_index
        self.error = False
        self.accumulator = 0
        self.ran_commands = []
        self.run()

    def run(self):
        while not self.error and not self.index >= len(self.program):
            if self.index in self.ran_commands:
                self.error = True
            else:
                self.ran_commands.append(self.index)
                command = "_BootCodeMachine__{}".format(self.program[self.index][0])
                getattr(self, command)(int(self.program[self.index][1]))

    def __acc(self, op):
        self.index += 1
        self.accumulator += op

    def __jmp(self, op):
        self.index += op

    def __nop(self, op):
        self.index += 1

