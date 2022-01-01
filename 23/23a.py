import copy
import sys
from datetime import datetime
import json

# state = {
#    "R1": ["C", "C"],
#    "R2": ["A", "A"],
#    "R3": ["B", "D"],
#    "R4": ["D", "B"],
#    "Q1": [".", "."],
#    "Q2": [".", "."],
#    "B1": ["."],
#    "B2": ["."],
#    "B3": ["."],
# }
#
#
# goalstate = {
#    "R1": ["A", "A"],
#    "R2": ["B", "B"],
#    "R3": ["C", "C"],
#    "R4": ["D", "D"],
#    "Q1": [".", "."],
#    "Q2": [".", "."],
#    "B1": ["."],
#    "B2": ["."],
#    "B3": ["."],
# }

state = {
    "R1": ["C", "D", "D", "C"],
    "R2": ["A", "C", "B", "A"],
    "R3": ["B", "B", "A", "D"],
    "R4": ["D", "A", "C", "B"],
    "Q1": [".", "."],
    "Q2": [".", "."],
    "B1": ["."],
    "B2": ["."],
    "B3": ["."],
}


goalstate = {
    "R1": ["A", "A", "A", "A"],
    "R2": ["B", "B", "B", "B"],
    "R3": ["C", "C", "C", "C"],
    "R4": ["D", "D", "D", "D"],
    "Q1": [".", "."],
    "Q2": [".", "."],
    "B1": ["."],
    "B2": ["."],
    "B3": ["."],
}


via = {
    "R1-R2": ["B1"],
    "R1-R3": ["B1", "B2"],
    "R1-R4": ["B1", "B2", "B3"],
    "R2-R1": ["B1"],
    "R2-R3": ["B2"],
    "R2-R4": ["B2", "B3"],
    "R3-R1": ["B1", "B2"],
    "R3-R2": ["B2"],
    "R3-R4": ["B3"],
    "R4-R1": ["B1", "B2", "B3"],
    "R4-R2": ["B2", "B3"],
    "R4-R3": ["B3"],
    "Q1-R2": ["B1"],
    "Q1-R3": ["B1", "B2"],
    "Q1-R4": ["B1", "B2", "B3"],
    "Q2-R1": ["B1", "B2", "B3"],
    "Q2-R2": ["B2", "B3"],
    "Q2-R3": ["B3"],
    "B1-R3": ["B2"],
    "B1-R4": ["B2", "B3"],
    "B2-R1": ["B1"],
    "B2-R4": ["B3"],
    "B3-R1": ["B1", "B2"],
    "B3-R2": ["B2"],
}


dist = {
    "R1-Q1": 2,
    "R2-Q1": 4,
    "R3-Q1": 6,
    "R4-Q1": 8,
    "R1-Q2": 8,
    "R2-Q2": 6,
    "R3-Q2": 4,
    "R4-Q2": 2,
    "R1-B1": 2,
    "R1-B2": 4,
    "R1-B3": 6,
    "R2-B1": 2,
    "R2-B2": 2,
    "R2-B3": 4,
    "R3-B1": 4,
    "R3-B2": 2,
    "R3-B3": 2,
    "R4-B1": 6,
    "R4-B2": 4,
    "R4-B3": 2,
    "R1-R2": 4,
    "R1-R3": 6,
    "R1-R4": 8,
    "R2-R1": 4,
    "R2-R3": 4,
    "R2-R4": 6,
    "R3-R1": 6,
    "R3-R2": 4,
    "R3-R4": 4,
    "R4-R1": 8,
    "R4-R2": 6,
    "R4-R3": 4,
}

home = {
    "R1": "a",
    "R2": "b",
    "R3": "c",
    "R4": "d",
    "A": "R1",
    "B": "R2",
    "C": "R3",
    "D": "R4",
}

scorefactor = {
    "A": 1,
    "B": 10,
    "C": 100,
    "D": 1000,
}

R = ["R1", "R2", "R3", "R4"]


def available_moves(state):
    def pathblocked(a, b):
        k = a + "-" + b
        if k in via.keys():
            for b in via[a + "-" + b]:
                if state[b][0] != ".":
                    return True
        return False

    mv = []
    rl = len(state["R1"]) - 1

    # Check pods in place, convert to lower case

    for r in R:

        for i in range(rl, -1, -1):
            if i == rl:
                if r == "R1" and state[r][i] == "A":
                    state[r][i] = state[r][i].lower()
            else:
                if r == "R1" and state[r][i + 1] == "a":
                    if r == "R1" and state[r][i] == "A":
                        state[r][i] = state[r][i].lower()

            if i == rl:
                if r == "R2" and state[r][i] == "B":
                    state[r][i] = state[r][i].lower()
            else:
                if r == "R2" and state[r][i + 1] == "b":
                    if r == "R2" and state[r][i] == "B":
                        state[r][i] = state[r][i].lower()

            if i == rl:
                if r == "R3" and state[r][i] == "C":
                    state[r][i] = state[r][i].lower()
            else:
                if r == "R3" and state[r][i + 1] == "c":
                    if r == "R3" and state[r][i] == "C":
                        state[r][i] = state[r][i].lower()

            if i == rl:
                if r == "R4" and state[r][i] == "D":
                    state[r][i] = state[r][i].lower()
            else:
                if r == "R4" and state[r][i + 1] == "d":
                    if r == "R4" and state[r][i] == "D":
                        state[r][i] = state[r][i].lower()

    # Moves from Rx to Qx
    # print(state)
    for r in R:
        br = False
        for i in range(0, len(state[r])):
            if state[r][i] == "." or state[r][i].islower():
                continue

            for q in ("Q1", "Q2"):

                if pathblocked(q, r):
                    continue

                for j in range(0, 2):
                    if state[q][j] == ".":
                        d = dist[r + "-" + q] + j + i
                        mv.append(((r, i), (q, j), d))
                        br = True
                    else:
                        break
            if br:
                break

    # Moves from Qx to Rx

    for q in ("Q1", "Q2"):
        br = False
        for i in range(0, len(state[q])):
            if state[q][i] == ".":
                continue

            for r in R:

                if pathblocked(q, r):
                    continue

                for j in range(len(state[r]) - 1, -1, -1):
                    if state[r][j] == "." and state[q][i].upper() == home[r].upper():
                        d = dist[r + "-" + q] + i + j
                        mv.append(((q, i), (r, j), d))
                        break
                    elif state[r][j].upper() != home[r].upper():
                        break

    # Moves from Rx to Rx

    for s in R:
        br = False
        for i in range(0, rl + 1):
            if state[s][i] == ".":
                continue
            if state[s][i] not in home.keys():
                break
            r = home[state[s][i]]
            if s == r:
                break
            if pathblocked(s, r):
                break
            for j in range(rl, -1, -1):
                if state[r][j] == ".":
                    d = dist[s + "-" + r] + i + j
                    mv.append(((s, i), (r, j), d))
                    br = True
                    break
                elif state[r][j].upper() != home[r].upper():
                    br = True
                    break
            if br:
                break

    # Moves from Rx to Bx

    for b in ("B1", "B2", "B3"):
        if state[b][0] != ".":
            continue

        for r in R:

            if pathblocked(b, r):
                continue

            for i in range(0, len(state[r])):
                if state[r][i] == "." or state[r][i].islower():
                    continue
                d = dist[r + "-" + b] + i
                mv.append(((r, i), (b, 0), d))
                break

    # Moves from Bx to Rx

    for b in ("B1", "B2", "B3"):
        br = False
        if state[b][0] == ".":
            continue

        for r in R:
            if pathblocked(b, r):
                continue

            for j in range(len(state[r]) - 1, -1, -1):
                if state[r][j] == "." and state[b][0].upper() == home[r].upper():
                    d = dist[r + "-" + b] + j
                    mv.append(((b, 0), (r, j), d))
                    break
                elif state[r][j].upper() != home[r].upper():
                    break

    if len(mv) > 0:
        return mv
    else:
        return None


def makemove(depth, score, state, path):

    global lowestscore
    global statecache

    h = hash(json.dumps(state))
    if h in statecache.keys():
        return statecache[h]

    thisstate = copy.deepcopy(state)
    moves = available_moves(thisstate)
    thisstate.clear()

    result = []
    if moves is not None:
        depth += 1
        for m in moves:
            nextstate = copy.deepcopy(state)
            t = m[2] * scorefactor[nextstate[m[0][0]][m[0][1]]]
            s = score + t

            if s <= lowestscore:

                nextstate[m[1][0]][m[1][1]] = nextstate[m[0][0]][m[0][1]]
                nextstate[m[0][0]][m[0][1]] = "."

                if nextstate == goalstate:
                    if s < lowestscore:
                        lowestscore = s
                    return t
                else:
                    r = makemove(depth, s, nextstate, path + ":" + json.dumps(m))
                    h = hash(json.dumps(nextstate))
                    statecache[h] = r
                    if r is not None:
                        result.append((t + r))
    if len(result) > 0:
        return min(result)
    else:
        return None


def main():
    global lowestscore
    global statecache
    lowestscore = 99999999
    statecache = {}
    res = makemove(0, 0, state, "")
    print(res)


if __name__ == "__main__":
    main()
