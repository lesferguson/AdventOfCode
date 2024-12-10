from operator import itemgetter
from fractions import Fraction
from numpy import exp, abs, angle

import numpy as np
data = open("Day10input.txt", "r")
orig_offset = (17, 22)

ast_loc = []
for y, row in enumerate(data.readlines()):
    for x, val in enumerate(row.strip()):
        if val == "#":
            cart = (float(x-orig_offset[0]), float(y-orig_offset[1]))
            if cart == (0.0, 0.0):
                continue
            rho = abs(np.sqrt(cart[0]**2 + cart[1]**2))
            phi = np.arctan2(cart[1], cart[0])
            z = cart[0] + 1j * cart[1]
            ast_loc.append((abs(z), angle(z)))
            # ast_loc.append(cart)

d_by_phi = {}
for point in ast_loc:
    if point[1] not in d_by_phi:
        d_by_phi[point[1]] = [point[0]]
    else:
        d_by_phi[point[1]].append(point[0])
i = 0
n=0
while True:

    for phi in sorted(d_by_phi.keys()):
        d_by_phi[phi].sort(reverse=True)
        if n == 0 and phi < -np.pi/2:
            continue

        if d_by_phi[phi]:
            z = d_by_phi[phi][-1] * exp(1j * (phi))
            if i == 2000:
                print(int(round(z.real))+orig_offset[0], int(round(z.imag))+orig_offset[1])
                break
            else:
                print(int(round(z.real))+orig_offset[0], int(round(z.imag))+orig_offset[1])

                d_by_phi[phi].pop()
                i += 1
    n += 1
    if i == 2000:
        break
#
# view_counts ={}
# for ast in ast_loc:
#     ast_paths = []
#     # (slope, 0=before/1=after)
#     for v in ast_loc:
#         if v == ast:
#             continue
#         x_diff = int(v[0] - ast[0])
#         y_diff = int(v[1] - ast[1])
#         if x_diff == 0:
#             m = ("inf", (y_diff / abs(y_diff)), 0)
#         elif y_diff == 0:
#             m = (0, 0, (x_diff/abs(x_diff)))
#         else:
#             m = (Fraction(y_diff, x_diff), (y_diff / abs(y_diff)), (x_diff / abs(x_diff)))
#         if m not in ast_paths:
#             ast_paths.append(m)
#     view_counts[ast] = len(ast_paths)
#
# m = max(view_counts.items(), key=itemgetter(1))[0]
# print(m, view_counts[m])


pass