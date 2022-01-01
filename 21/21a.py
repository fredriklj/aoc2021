import numpy as np

p1_start = 8
p2_start = 2
p1_score = p2_score = 0

p1_pos = np.roll(np.arange(10) + 1, -p1_start)
p2_pos = np.roll(np.arange(10) + 1, -p2_start)
dice = np.arange(100) + 1

rolls = 0

while True:

    p1_roll = p2_roll = 0
    for p1 in range(0, 3):
        p1_roll += dice[0]
        dice = np.roll(dice, -1)

    p1_pos = np.roll(p1_pos, -p1_roll)
    p1_score += p1_pos[-1]
    rolls += 3

    print(
        "P1 pos is %s after rolling %s times, score is %s" % (p1_pos, rolls, p1_score)
    )

    if p1_score >= 1000:
        break

    for p2 in range(0, 3):
        p2_roll += dice[0]
        dice = np.roll(dice, -1)

    p2_pos = np.roll(p2_pos, -p2_roll)
    p2_score += p2_pos[-1]
    rolls += 3

    print(
        "P2 pos is %s after rolling %s times, score is %s" % (p2_pos, rolls, p2_score)
    )

    if p2_score >= 1000:
        break

print(p2_score * rolls)
