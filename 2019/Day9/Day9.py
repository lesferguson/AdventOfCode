from intcode import intcode
from collections import deque


program = intcode([int(option) for option in open("Day9input.txt", "r").read().split(",")]).loop()
