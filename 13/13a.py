import numpy as np

inp = []
f = "input3-1.txt"
f2 = "input3-2.txt"

xarr = []
yarr = []

folding = []

for line in open(f2).readlines():
    (x, y) = line.strip().split("=")
    folding.append((x, int(y)))

for line in open(f).readlines():
    (x, y) = line.strip().split(",")
    xarr.append(int(x))
    yarr.append(int(y))

xmax = max(xarr)
ymax = max(yarr)

a = np.zeros([ymax + 1, xmax + 1])

for i in range(0, len(xarr)):
    a[yarr[i], xarr[i]] = 1

a = np.flip(a)

for f in folding:
    if f[0] == "y":
        padding = f[1] * 2 + 1 - a.shape[0]
        if padding > 0:
            a = np.pad(a, ((padding, 0), (0, 0)), mode="constant", constant_values=0)
        elif padding < 0:
            a = np.pad(a, ((0, padding), (0, 0)), mode="constant", constant_values=0)
        a = np.delete(a, (f[1] + padding), axis=0)

        fold = np.vsplit(a, 2)
        a = fold[0] + np.flip(fold[1], axis=0)

    else:
        padding = f[1] * 2 + 1 - a.shape[1]
        if padding > 0:
            a = np.pad(a, ((0, 0), (0, padding)), mode="constant", constant_values=0)
        elif padding < 0:
            a = np.pad(a, ((0, 0), (padding, 0)), mode="constant", constant_values=0)

        a = np.delete(a, (f[1]), axis=1)
        fold = np.hsplit(a, 2)
        a = fold[0] + np.flip(fold[1], axis=1)

a[a > 0] = 1
np.set_printoptions(threshold=np.inf, linewidth=180)
print(np.array2string(a).replace("0.", "  "))
