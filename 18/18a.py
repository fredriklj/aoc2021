import re
import json

f = "input.txt"


def explode(inp):
    # find position, if any
    c = 0
    for p in range(0, len(inp)):
        if inp[p] == "[":
            c += 1
        if inp[p] == "]":
            c += -1
        if c == 5:
            # find position and length of element to explode
            m = re.search(r"\[[0-9,]+\]", inp[p:])
            tupl = m.span(0)[1]
            tup = inp[p : p + tupl]
            l, r = re.findall(r"[0-9]+", tup)
            l_shunk, r_shunk = inp[:p], inp[p + tupl :]

            # find l position and add to
            m = re.search(r"\d+(?=\D*$)", l_shunk)
            if m is not None:
                l_rep = int(l_shunk[m.span(0)[0] : m.span(0)[1]]) + int(l)
                l_shunk = l_shunk[: m.span(0)[0]] + str(l_rep) + l_shunk[m.span(0)[1] :]

            # find r position and add to
            m = re.search(r"[0-9]+", r_shunk)
            if m is not None:
                r_rep = int(r_shunk[m.span(0)[0] : m.span(0)[1]]) + int(r)
                r_shunk = r_shunk[: m.span(0)[0]] + str(r_rep) + r_shunk[m.span(0)[1] :]

            # replace exploded element with 0
            inp = l_shunk + "0" + r_shunk
            return inp

    return None


def split(inp):
    # find position, if any
    m = re.search(r"[0-9]{2}", inp)
    if m is not None:
        l_pos, r_pos = m.span(0)[0], m.span(0)[1]
        i = int(inp[l_pos:r_pos])
        l_shunk, r_shunk = inp[:l_pos], inp[r_pos:]
        ins = "[" + str(int(i / 2)) + "," + str(int((i + 1) / 2)) + "]"
        return l_shunk + ins + r_shunk
    return None


def depth(L):
    return isinstance(L, list) and max(map(depth, L)) + 1


def add(a, b):
    return "[" + a + "," + b + "]"


def magnitude(data):
    l = data[0]
    r = data[1]

    if isinstance(l, list):
        if depth(l) == 1:
            magn = l[0] * 3 + l[1] * 2
            l = magn
        else:
            l = magnitude(l)

    if isinstance(r, list):
        if depth(r) == 1:
            magn = r[0] * 3 + r[1] * 2
            r = magn
        else:
            r = magnitude(r)

    return l * 3 + r * 2


inp = ""
for line in open(f).readlines():
    row = line.strip()
    if len(inp) > 0:
        inp = add(inp, row)
        while True:
            i = explode(inp)
            if i is None:
                s = split(inp)
                if s is None:
                    break
                else:
                    inp = s
            else:
                inp = i
    else:
        inp = row

print(inp)
data = json.loads(inp)
res = magnitude(data)
print(res)
