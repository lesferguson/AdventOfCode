from collections import deque
import sys


class intcode():
    def __init__(self, prg: list):
        self.prg = prg + [0] * 10000
        self.i = 0
        self.rb = 0

    def loop(self, inputs=deque()):
        while True:
            code = str(self.prg[self.i])
            code = (5 - len(code)) * "0" + code
            index = {}
            for n in range(3, 6):
                if code[-n] == "1":
                    index[n - 2] = self.i + n - 2
                elif code[-n] == "2":
                    index[n - 2] = self.rb + self.prg[self.i + n - 2]
                else:
                    try:
                        index[n - 2] = self.prg[self.i + n - 2]
                    except:
                        pass
            # print(self.i, self.rb, code, self.prg[self.i:self.i+4], self.prg[index)

            if code.endswith("99"):
                return "Halt"
            elif code.endswith("01"):
                self.prg[index[3]] = self.prg[index[1]] + self.prg[index[2]]
                self.i += 4
            elif code.endswith("02"):
                self.prg[index[3]] = self.prg[index[1]] * self.prg[index[2]]
                self.i += 4
            elif code.endswith("03"):
                if inputs:
                    s = inputs.popleft()
                else:
                    s = input("Input:")

                self.prg[index[1]] = int(s)
                self.i += 2
            elif code.endswith("04"):
                self.i += 2
                return int(self.prg[index[1]])

            elif code.endswith("05"):
                target = self.prg[index[1]]
                if target != 0:
                    self.i = self.prg[index[2]]
                else:
                    self.i += 3
            elif code.endswith("06"):
                target = self.prg[index[1]]
                if target == 0:
                    self.i = self.prg[index[2]]
                else:
                    self.i += 3
            elif code.endswith("07"):
                if self.prg[index[1]] < self.prg[index[2]]:
                    self.prg[index[3]] = 1
                else:
                    self.prg[index[3]] = 0
                self.i += 4
            elif code.endswith("08"):
                if self.prg[index[1]] == self.prg[index[2]]:
                    self.prg[index[3]] = 1
                else:
                    self.prg[index[3]] = 0
                self.i += 4
            elif code.endswith("09"):
                self.rb += self.prg[index[1]]
                self.i += 2
            else:
                print(f"{self.i} - {code}")
                sys.exit(1)
