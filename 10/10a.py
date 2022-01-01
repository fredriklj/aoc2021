br = {")": "(", "]": "[", "}": "{", ">": "<"}
score = {")": 3, "]": 57, "}": 1197, ">": 25137}
inp = []
res = 0
f = "input2.txt"


def b0rken(arr):

    check = []
    for c in arr:
        if c not in br.keys():
            check.append(c)
        else:
            if br[c] == check[-1]:
                check.pop()
            else:
                return score[c]
    return 0


for line in open(f).readlines():
    inp.append([c for c in line.strip()])

for i in inp:
    res += b0rken(i)

print(res)
