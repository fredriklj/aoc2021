import numpy as np

inp = []

for line in open("input2.txt").readlines():
    inp.append([int(c) for c in line.strip()])

arr = np.array(inp)


def lmin(matrix):
    return (
        (matrix < np.roll(matrix, 1, 0))
        & (matrix < np.roll(matrix, -1, 0))
        & (matrix < np.roll(matrix, 1, 1))
        & (matrix < np.roll(matrix, -1, 1))
    )


def floodsum(matrix, x, y):
    if matrix[x][y] == 9:
        return 0
    elif matrix[x][y] == -1:
        return 0
    else:
        matrix[x][y] = -1
        return (
            1
            + floodsum(matrix, x - 1, y)
            + floodsum(matrix, x, y - 1)
            + floodsum(matrix, x, y + 1)
            + floodsum(matrix, x + 1, y)
        )


arr = np.pad(arr, (1, 1), "maximum")
min = np.where(lmin(arr + 1) * (arr + 1) > 0)

b = []

for i in range(len(min[0])):
    b.append(floodsum(arr, min[0][i], min[1][i]))

b.sort(reverse=True)

print(b[0] * b[1] * b[2])
