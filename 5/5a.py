import numpy as np

matrix = np.zeros((1000, 1000), int)


def draw_line(mat, c):
    [x0, y0] = [c[0][0], c[0][1]]
    [x1, y1] = [c[1][0], c[1][1]]

    if (x0, y0) == (x1, y1):
        mat[x0, y0] += 1
        return mat

    transpose = abs(x1 - x0) < abs(y1 - y0)

    if transpose:
        mat = mat.T
        x0, y0, x1, y1 = y0, x0, y1, x1

    if x0 > x1:
        x0, y0, x1, y1 = x1, y1, x0, y0

    mat[x0, y0] += 1
    mat[x1, y1] += 1
    x = np.arange(x0 + 1, x1)
    y = np.round(((y1 - y0) / (x1 - x0)) * (x - x0) + y0).astype(x.dtype)
    mat[x, y] += 1


for line in open("input2.txt").readlines():
    coordinates = [
        list(map(int, lst))
        for lst in [x.split(",") for x in (line.strip().split(" -> "))]
    ]
    if coordinates[0][1] == coordinates[1][1] or coordinates[0][0] == coordinates[1][0]:
        draw_line(matrix, coordinates)

print((matrix > 1).sum())
