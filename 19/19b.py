import numpy as np
import re
import sys

f = "input1.txt"

np.set_printoptions(threshold=np.inf)


def matchtest(m, n):
    xmatch = ymatch = zmatch = False
    xflipped = yflipped = zflipped = False
    swappedxy = swappedxz = swappedyz = False
    n_rows, n_columns = n.shape
    axisswap = 0
    rounds = 0

    # first we test if matrices match without rotation or axis swapping
    while not all([xmatch, ymatch, zmatch]):
        # Init testing matrix and add values from n[0] to all rows
        test = m + n[0]
        for a in range(1, n_rows):
            # Append m matrix with n[row] added to all rows
            test = np.append(test, m + n[a], axis=0)

        # Now we have a long test matrix where each copy of m has the values of each of the rows of n added to it

        # See if we got at least 12 same x-values from addition
        if xmatch == False:
            uni, freq = np.unique(test[:, 0], return_counts=True)
            xmatches = uni[np.where(freq >= 12)]
            if len(xmatches) > 0:
                xmatch = True
                # print("We got match (%s) on x-axis" % (matches))
                xoffset = xmatches[0]
            else:
                if xflipped == False:
                    # Lets try to flip x-axis orientation for the next round
                    # print("Flipping x orientation")
                    n = n * [-1, 1, 1]
                    xflipped = True

        # See if we got at least 12 same y-values from addition
        if ymatch == False:
            uni, freq = np.unique(test[:, 1], return_counts=True)
            ymatches = uni[np.where(freq >= 12)]
            if len(ymatches) > 0:
                ymatch = True
                # print("We got match (%s) on y-axis" % (matches))
                yoffset = ymatches[0]
            else:
                if yflipped == False:
                    # Lets try to flip y-axis orientation for the next round
                    # print("Flipping y orientation")
                    n = n * [1, -1, 1]
                    yflipped = True

        # See if we got at least 12 same z-values from addition
        if zmatch == False:
            uni, freq = np.unique(test[:, 2], return_counts=True)
            apa, bepa = uni, freq
            zmatches = uni[np.where(freq >= 12)]
            if len(zmatches) > 0:
                zmatch = True
                # print("We got match (%s) on z-axis" % (matches))
                zoffset = zmatches[0]
            else:
                if zflipped == False:
                    # Lets try to flip y-axis orientation for the next round
                    # print("Flipping z orientation")
                    n = n * [1, 1, -1]
                    zflipped = True

        if (
            swappedxy == False
            and xmatch == False
            and ymatch == False
            and xflipped == True
            and yflipped == True
        ):
            # swap x-y
            n[:, [0, 1]] = n[:, [1, 0]]
            xflipped = yflipped = zflipped = False
            swappedxy = True
            swappedxz = False
            swappedyz = False
            xmatch = ymatch = zmatch = False
            # print("Swapped axis x-y")

        if (
            swappedxz == False
            and xmatch == False
            and zmatch == False
            and xflipped == True
            and zflipped == True
        ):
            # swap x-z
            n[:, [0, 2]] = n[:, [2, 0]]
            xflipped = yflipped = zflipped = False
            swappedxy = False
            swappedxz = True
            swappedyz = False
            xmatch = ymatch = zmatch = False
            # print("Swapped axis x-z")

        if (
            swappedyz == False
            and ymatch == False
            and zmatch == False
            and yflipped == True
            and zflipped == True
        ):
            # swap y-z
            n[:, [1, 2]] = n[:, [2, 1]]
            xflipped = yflipped = zflipped = False
            xmatch = ymatch = zmatch = False
            swappedxy = False
            swappedxz = False
            swappedyz = True
            # print("Swapped axis y-z")

        if rounds > 12:
            # print("No match could be found")
            return None, None

        rounds += 1

    # Now we offset n matrix to the position of m
    n = n - [xoffset, yoffset, zoffset]
    n = -n

    # Sort for visibility
    # n = n[n[:,0].argsort()]
    # m = m[m[:,0].argsort()]

    return (xoffset, yoffset, zoffset), n


sn = 0
s = {}
scanner = {}

for line in open(f).readlines():
    row = line.strip()
    if re.match(r"^--- scanner", row):
        sn += 1
        scanner[sn] = []
    elif re.match(r"^[0-9,-]+$", row):
        scanner[sn].append(list(map(int, row.split(","))))


for i in range(1, sn + 1):
    s[i] = np.array(scanner[i])


hits = [1]
offsets = []

while len(hits) > 0:
    j = hits.pop(0)
    for i in range(1, sn + 1):
        if j != i:
            foo, bar = matchtest(s[j], s[i])
            if bar is not None:
                print("Matrix %s is adjecent with %s" % (j, i))
                print("Aligning %s with %s at offset %s" % (i, j, foo))
                s[i] = bar
                hits.append(i)
                offsets.append(foo)


scanners = np.array(offsets)
x, y = scanners.shape
distance = []

for i in range(0, x):
    for j in range(i, x):
        dist = np.sum(np.absolute(scanners[i] - scanners[j]))
        distance.append(dist)

print(max(distance))
