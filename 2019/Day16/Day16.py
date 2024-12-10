import numpy as np


inbound = [int(digit.strip()) for digit in open("Day16input.txt", "r").read()] *10000
offset = int("".join([str(digit) for digit in inbound[:7]]))
base_operations = [0, 1, 0, -1]

operations_list = []
for i in range(1, len(inbound) + 1):
    operations_temp = [val for val in base_operations for __ in range(i)]
    if len(operations_temp) < len(inbound) + 1:
        operations = operations_temp * (len(inbound) // len(operations_temp) + 1)
    else:
        operations = operations_temp
    operations = operations[1:len(inbound) + 1]
    operations_list.append(operations)


n = 0
while n < 100:
    n += 1
    out = []
    # for i in range(0, len(inbound)):
    #     # out_val = 0
    #     # for j in range(len(inbound)):
    #     #     out_val += inbound[j] * operations[j]
    #
    #     out_val = np.sum(np.multiply(operations_list[i], inbound))
    #     out.append(int(str(out_val)[-1]))

    # out_test = [int(str(v)[-1]) for v in [np.sum(np.multiply(operations_list[j], inbound)) for j in range(0, len(inbound))]]
    out_test = [int(str(np.sum(np.multiply(operations_list[j], inbound)))[-1]) for j in range(0, len(inbound))]
    inbound = out_test
    print(out[offset:offset+8])
    # print(out_test[:8])
