t = 0
dmap = {}
infile = "input2.txt"


def is_in(a, b):
    ret = 0
    c = [c for c in a]
    for c in a:
        if c in b:
            ret += 1

    return ret == len(a)


for line in open(infile).readlines():

    (i, o) = line.strip().split(" | ")
    l = ["".join(sorted(e)) for e in sorted(i.split(" "), key=len)]

    dmap[1] = l[0]
    dmap[4] = l[2]
    dmap[7] = l[1]
    dmap[8] = l[9]

    ## 6-ställiga nummer: 0, 6, 9
    ##
    ## Om X inte innehåller hela "1", X = "6"
    ## Om X innehåller hela "4", X = "9"
    ## Annars, X = "0"

    for i in range(6, 9):  # sexställigt
        if not (dmap[1][0] in l[i] and dmap[1][1] in l[i]):
            dmap[6] = l[i]
        elif is_in(dmap[4], l[i]):
            dmap[9] = l[i]
        else:
            dmap[0] = l[i]

    ## 5-ställiga nummer: 5, 3, 2
    ## Om X innehåller hela "6", X = "5"
    ## Om X innehåller hela "9", X = "3"
    ## Annars, X = "2"

    for i in range(3, 6):  # femställigt
        if is_in(l[i], dmap[6]):
            dmap[5] = l[i]
        elif is_in(l[i], dmap[9]):
            dmap[3] = l[i]
        else:
            dmap[2] = l[i]

    xmap = {dmap[k]: k for k in dmap}

    o = o.split(" ")
    d = 0

    for i in range(0, 4):
        d += xmap["".join(sorted(o[i]))] * (10 ** (3 - i))

    # print("Decoded", d)

    t += d

print(t)
