br = {")": "(", "]": "[", "}": "{", ">": "<"}
rb = {br[k]: k for k in br}
score = {")": 1, "]": 2, "}": 3, ">": 4}
inp = []
scores = []
res = 0
f = "input2.txt"


def nonb0rken(arr):
    check = []
    for c in arr:
        if c not in br.keys():
            check.append(c)
        else:
            if br[c] == check[-1]:
                check.pop()
            else:
                return False
    return True


def complete(arr):
    rest = []
    for c in arr:
        if c not in br.keys():
            rest.append(c)
        else:
            if br[c] == rest[-1]:
                rest.pop()
    return rest


def mirror(arr):
    res = []
    for c in arr:
        res[:0] = rb[c]
    return res


def countscore(arr):
    res = 0
    for c in arr:
        res = res * 5 + score[c]
    return res


for line in open(f).readlines():
    inp.append([c for c in line.strip()])

incomplete = filter(nonb0rken, inp)

for i in incomplete:
    scores.append(countscore(mirror(complete(i))))

scores.sort()
print(scores[int((len(scores) - 1) / 2)])
