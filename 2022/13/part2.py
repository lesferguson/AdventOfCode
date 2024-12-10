import json
from copy import deepcopy

def compare_lists(left_list, right_list):
    while True:
        if len(left_list) == 0 and len(right_list) == 0:
            return
        if len(left_list) == 0:
            raise ConnectionAbortedError
        if len(right_list) == 0:
            raise ConnectionRefusedError
        left = left_list.pop(0)
        right = right_list.pop(0)
        if type(left) == list or type(right) == list:
            if type(left) != list:
                left = [left]
            if type(right) != list:
                right = [right]
            compare_lists(left, right)

        else:
            if left < right:
                raise ConnectionAbortedError
            elif left > right:
                raise ConnectionRefusedError


def run(data):
    inputs = [json.loads(line) for line in data if line]
    inputs.append([[2]])
    inputs.append([[6]])
    right_order = []

    #
    # for pair in range(0, int(len(inputs)), 2):
    #         left = inputs[pair]
    #         right = inputs[pair+1]
    #         try:
    #             compare_lists(left, right)
    #         except ConnectionAbortedError:
    #             right_order.append(int(pair/2+1))
    #         except ConnectionRefusedError:
    #             pass
    #         else:
    #             pass

    n = len(inputs)
    # optimize code, so if the array is already sorted, it doesn't need
    # to go through the entire process
    swapped = False
    # Traverse through all array elements
    for i in range(n - 1):
        # range(n) also work but outer loop will
        # repeat one time more than needed.
        # Last i elements are already in place
        for j in range(0, n - i - 1):

            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            left = inputs[j]
            right = inputs[j + 1]
            try:
                compare_lists(deepcopy(left), deepcopy(right))
            except ConnectionAbortedError:
                pass
            except ConnectionRefusedError:
                swapped = True
                inputs[j], inputs[j + 1] = inputs[j + 1], inputs[j]

            #
            # if inputs[j] > inputs[j + 1]:
            #     swapped = True
            #     inputs[j], inputs[j + 1] = inputs[j + 1], inputs[j]

        if not swapped:
            # if we haven't needed to make a single swap, we
            # can just exit the main loop.
            break


    return (inputs.index([[2]])+1) * (inputs.index([[6]])+1)