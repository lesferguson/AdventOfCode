import json

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
    right_order = []
    for pair in range(0, int(len(inputs)), 2):
            left = inputs[pair]
            right = inputs[pair+1]
            try:
                compare_lists(left, right)
            except ConnectionAbortedError:
                right_order.append(int(pair/2+1))
            except ConnectionRefusedError:
                pass
            else:
                pass


    return sum(right_order)