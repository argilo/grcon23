#!/usr/bin/env python3

import itertools
import struct

TRANSITION_ITERATIONS = 160
HOLD_ITERATIONS = 40

f_in = open("points.txt")
paths = []
paths.append([[0.0, 0.0]])
path = []
for line in f_in:
    if line.startswith("#"):
        min_x = min([x for x, y in path])
        max_x = max([x for x, y in path])
        mid_x = (min_x + max_x) / 2

        new_path = []
        for x, y in path:
            new_x = (x - mid_x) / 150
            new_y = -(y - 172) / 150
            new_path.append([new_x, new_y])
        paths.append(new_path)

        path = []
    else:
        path.append([float(coord_str) for coord_str in line.rstrip().split(",")])

paths.append([[0.0, 0.0]])
f_in.close()

f_out = open("interpolated.c32", "wb")
for path1, path2 in itertools.pairwise(paths):
    l1 = len(path1)
    l2 = len(path2)
    lmax = max(len(path) for path in paths)
    for i in range(TRANSITION_ITERATIONS):
        for j in range(lmax):
            x1, y1 = path1[int(l1 * j / lmax)]
            x2, y2 = path2[int(l2 * j / lmax)]
            frac = i / TRANSITION_ITERATIONS
            x = x1 * (1 - frac) + x2 * frac
            y = y1 * (1 - frac) + y2 * frac
            f_out.write(struct.pack("ff", x, y))
    for i in range(HOLD_ITERATIONS):
        for j in range(lmax):
            x2, y2 = path2[int(l2 * j / lmax)]
            f_out.write(struct.pack("ff", x2, y2))
f_out.close()
