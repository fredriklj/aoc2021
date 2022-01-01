import numpy as np
from itertools import product

f = "input2.txt"
cube = {}

sum = 0
for line in open(f).readlines():
    l = line.strip()
    l1, l2 = line.split(" ")
    if l1 == "on":
        state = 1
    else:
        state = 0

    xr, yr, zr = l2.split(",")
    foo, xr = xr.split("=")
    xmin, xmax = xr.split("..")
    x = list(range(int(xmin), int(xmax) + 1))

    foo, yr = yr.split("=")
    ymin, ymax = yr.split("..")
    y = list(range(int(ymin), int(ymax) + 1))

    foo, zr = zr.split("=")
    zmin, zmax = zr.split("..")
    z = list(range(int(zmin), int(zmax) + 1))

    deletes = 0
    adds = 0

    for xp in range(0, len(x)):
        for yp in range(0, len(y)):
            for zp in range(0, len(z)):
                if state == 1:
                    cube[(x[xp], y[yp], z[zp])] = 1
                else:
                    if (x[xp], y[yp], z[zp]) in cube:
                        del cube[(x[xp], y[yp], z[zp])]

print(len(cube.keys()))
