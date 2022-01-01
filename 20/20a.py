import numpy as np

f1 = "input-alg.txt"
f2 = "input-img.txt"

np.set_printoptions(threshold=np.inf, linewidth=100000)

imgarr = []
algarr = []

for line in open(f2).readlines():
    l = line.strip()
    l = l.replace("#", "1")
    l = l.replace(".", "0")
    la = list(map(int, [c for c in l]))
    imgarr.append(la)

for line in open(f1).readlines():
    l = line.strip()
    l = l.replace("#", "1")
    l = l.replace(".", "0")
    algarr = list(map(int, [c for c in l]))

img = np.array(imgarr)
img = np.pad(img, ((75, 75), (75, 75)), mode="constant", constant_values=0)
imgx, imgy = img.shape
out = np.zeros([imgx, imgy], dtype=int)
alg = np.array(algarr)

for i in range(0, 50):
    out = np.zeros([imgx, imgy], dtype=int)
    if i % 2 == 0 and alg[0] == 1:
        out = np.where(out == 0, 1, out)
        padval = 1
    else:
        padval = 0
    # padval = 0

    for x in range(2, imgx - 2):
        for y in range(2, imgy - 2):
            foc = img[x - 1 : x + 2, y - 1 : y + 2]
            b = foc.reshape(9).tolist()
            bs = "".join(list(map(str, b)))
            n = int(bs, 2)
            out[x][y] = int(algarr[n])

    out = out[3:-3, 3:-3]
    out = np.pad(out, ((3, 3), (3, 3)), mode="constant", constant_values=padval)
    img = out

foo = out[out > 0]
print(len(foo))
