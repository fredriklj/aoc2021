import numpy as np

inp = []
f = "input2.txt"


def flash(m, c):
    for x, y in c:
        xmax, ymax = m.shape
        x1 = max(0, x - 1)
        x2 = min(xmax, x + 2)
        y1 = max(0, y - 1)
        y2 = min(ymax, y + 2)

        slajs = m[x1:x2, y1:y2]
        slajs += 1
        slajs[slajs == 11] = 10
        m[x1:x2, y1:y2] = slajs
        m[x, y] += 1

    b = np.where(m == 10)
    b = np.column_stack((b[0], b[1]))
    if b.shape[0] > 0:
        flash(m, b)


for line in open(f).readlines():
    inp.append([int(c) for c in line.strip()])

a = np.matrix(inp)

sum = 0

for i in range(0, 100):

    a += 1
    b = np.where(a == 10)
    b = np.column_stack((b[0], b[1]))
    flash(a, b)
    a[a > 9] = 0
    sum += len(np.where(a == 0)[0])

print(sum)
