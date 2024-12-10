from collections import defaultdict


def run(data):
    plane = defaultdict(int, {})
    for line in data:
        a_raw, b_raw = line.split(" -> ")
        a = tuple(a_raw.split(","))
        b = tuple(b_raw.split(","))
        if a[0] == b[0]:

            y_dir = int((int(b[1]) - int(a[1])) / (abs(int(b[1]) - int(a[1]))))
            for i in range(int(a[1]), int(b[1]) + y_dir, y_dir):
                plane[(int(a[0]), i)] += 1

        elif a[1] == b[1]:
            x_dir = int((int(b[0]) - int(a[0])) / abs(int(b[0]) - int(a[0])))

            for i in range(int(a[0]), int(b[0]) + x_dir, x_dir):
                plane[(i, int(a[1]))] += 1
        else:
            x_dir = int((int(b[0]) - int(a[0])) / abs(int(b[0]) - int(a[0])))
            y_dir = int((int(b[1]) - int(a[1])) / (abs(int(b[1]) - int(a[1]))))
            x_coords = []
            for i in range(int(a[0]), int(b[0]) + x_dir, x_dir):
                x_coords.append(i)
            y_coords = []
            for j in range(int(a[1]), int(b[1]) + y_dir, y_dir):
                y_coords.append(j)

            for n in range(len(y_coords)):
                plane[x_coords[n], y_coords[n]] += 1

    safe_points = 0
    for k, v in plane.items():
        if v >= 2:
            safe_points += 1

    return safe_points
