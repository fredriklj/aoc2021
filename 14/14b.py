import copy

f = "input2.txt"
input = "OKSBBKHFBPVNOBKHBPCO"

rounds = 40

m = {}

for line in open(f).readlines():
    a, b = line.strip().split(" -> ")
    m[a] = b

inp = list(input)

foo = {}
res = {}


def addval(v, a, m):
    if v in m.keys():
        m[v] += a
    else:
        m[v] = a


for i in inp:
    addval(i, 1, foo)

for i in range(0, len(inp) - 1):
    c = inp[i] + m[inp[i] + inp[i + 1]] + inp[i + 1]
    if c in res.keys():
        res[c] += 1
    else:
        res[c] = 1

    addval(m[inp[i] + inp[i + 1]], 1, foo)

nxt = copy.deepcopy(res)
res = {}

for i in range(0, rounds - 1):
    for k in nxt.keys():
        addval(m[k[0] + k[1]], nxt[k], foo)
        a = k[0] + m[k[0] + k[1]] + k[1]
        addval(a, nxt[k], res)
        b = k[1] + m[k[1] + k[2]] + k[2]
        addval(m[k[1] + k[2]], nxt[k], foo)
        addval(b, nxt[k], res)
    nxt = copy.deepcopy(res)
    res = {}

output = [v for k, v in sorted(foo.items(), key=lambda item: item[1])]
print(output[-1] - output[0])
