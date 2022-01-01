import numpy as np
from time import time

np.set_printoptions(threshold=np.inf, linewidth=100000)

f = "input6.txt"
cube = {}
matrices = []
operators = {}

sum = 0
for line in open(f).readlines():
    l = line.strip()
    l1, l2 = line.split(" ")
    if l1 == "on":
        op = 1
    else:
        op = 0

    xr, yr, zr = l2.split(",")
    foo, xr = xr.split("=")
    xmin, xmax = xr.split("..")

    foo, yr = yr.split("=")
    ymin, ymax = yr.split("..")

    foo, zr = zr.split("=")
    zmin, zmax = zr.split("..")

    dim = (int(xmin), int(xmax), int(ymin), int(ymax), int(zmin), int(zmax))
    matrices.append(dim)
    operators[dim] = op


x1 = []
x2 = []
y1 = []
y2 = []
z1 = []
z2 = []

sum = 0

zsteps = []
for m in matrices:
    zsteps.append(m[4])
    zsteps.append(m[5] + 1)

zsteps.sort()

timestart = time()

for s in range(0, len(zsteps) - 1):
    timeround = time()
    xmin = None
    xmax = None
    ymin = None
    ymax = None
    for m in matrices:
        if zsteps[s] >= m[4] and zsteps[s + 1] - 1 <= m[5]:
            if xmin is None:
                xmin = m[0]
                xmax = m[1]
                ymin = m[2]
                ymax = m[3]
            else:
                if m[0] < xmin:
                    xmin = m[0]
                if m[1] > xmax:
                    xmax = m[1]
                if m[2] < ymin:
                    ymin = m[2]
                if m[3] > ymax:
                    ymax = m[3]
    ax2 = -xmin
    ay2 = -ymin
    dx2 = xmax - xmin + 1
    dy2 = ymax - ymin + 1

    slajs = np.zeros((dx2, dy2), dtype=bool)
    for m in matrices:
        if zsteps[s] >= m[4] and zsteps[s + 1] - 1 <= m[5]:
            slajs[ax2 + m[0] : ax2 + m[1] + 1, ay2 + m[2] : ay2 + m[3] + 1] = operators[
                m
            ]
    sum += np.count_nonzero(slajs) * (zsteps[s + 1] - zsteps[s])
    print(
        "Round %s with a matrix of %s elements took %s seconds, %s seconds in total"
        % (s, dx2 * dy2, int(time() - timeround), int(time() - timestart))
    )

print(sum)
