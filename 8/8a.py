lengthmap = {2: 1, 3: 7, 4: 4, 5: [2, 3, 5], 6: [0, 6, 9], 7: 8}

for line in open("input2.txt").readlines():
    (i, o) = line.strip().split(" | ")
    for d in o.split(" "):
        if isinstance(lengthmap[len(d)], int):
            print(lengthmap[len(d)])
