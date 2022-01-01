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


arr = np.pad(arr + 1, (1, 1), "maximum")
arr = lmin(arr) * arr
arr = arr[1:-1, 1:-1]

# print(arr)

print(np.sum(arr))
