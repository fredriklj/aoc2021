import pandas as pd
import numpy as np

f = "input2.txt"

# np.set_printoptions(threshold=np.inf, linewidth=100000)

inp = []

for line in open(f).readlines():
    l = line.strip()
    chars = list(l)
    inp.append(chars)

matr = pd.DataFrame(inp)

print(matr)

dy, dx = matr.shape

xr1 = np.arange(dx)
xr2 = np.roll(xr1, -1)
yr1 = np.arange(dy)
yr2 = np.roll(yr1, -1)


# Move east

steps = 0
last = None

while not matr.equals(last):

    steps += 1
    print(steps)
    last = matr.copy()

    ## Move east

    flip = []

    for y in range(0, dy):
        for x in range(0, dx):
            if matr.iloc[y, xr1[x]] == ">":
                if matr.iloc[y, xr2[x]] == ".":
                    flip.append((y, xr1[x], xr2[x]))

    for f in flip:
        matr.iloc[f[0], f[1]] = "."
        matr.iloc[f[0], f[2]] = ">"

    ## Move south

    flip = []

    for x in range(0, dx):
        for y in range(0, dy):
            if matr.iloc[yr1[y], x] == "v":
                if matr.iloc[yr2[y], x] == ".":
                    flip.append((x, yr1[y], yr2[y]))

    for f in flip:
        matr.iloc[f[1], f[0]] = "."
        matr.iloc[f[2], f[0]] = "v"


print(matr)
