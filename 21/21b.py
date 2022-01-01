import numpy as np
from dataclasses import dataclass
from itertools import product
from collections import Counter
from collections import defaultdict


# p1_start = 8
# p2_start = 2

p1_start = 8
p2_start = 2

board = np.arange(10) + 1

dice = list(product("123", repeat=3))
dice = [list(map(int, d)) for d in dice]


@dataclass(unsafe_hash=True)
class Outcome:
    score: int = 0
    pos: int = 0


def round(state: Outcome):

    scenarios = []
    wins = 0

    for p1 in dice:

        p_score = state.score
        p_pos = state.pos

        p_move = sum(p1)
        p_pos = (p_pos + p_move) % 10
        if p_pos == 0:
            p_pos = 10
        p_score += p_pos

        if p_score < 21:
            scenarios.append(Outcome(p_score, p_pos))
        else:
            wins += 1

    return scenarios, wins


p1_tot_wins = 0
p2_tot_wins = 0

p1_outcomes = p2_outcomes = i = 1

p1_round = {}
p2_round = {}
p1_round[Outcome(0, p1_start)] = 1
p2_round[Outcome(0, p2_start)] = 1


while p1_outcomes > 0 and p2_outcomes > 0:
    p1_aggregated = {}
    p2_aggregated = {}
    p1_wins = 0
    p2_wins = 0
    p1_totoutcomes = 0
    p2_totoutcomes = 0

    p1_count = 0

    for p1_nextstep in p1_round.keys():

        p1_multiplier = p1_round[p1_nextstep]
        p1_count += p1_multiplier

        p1_oc, p1_w = round(p1_nextstep)

        for p1_outcome in p1_oc:
            if p1_outcome in p1_aggregated:
                p1_aggregated[p1_outcome] += p1_multiplier
            else:
                p1_aggregated[p1_outcome] = p1_multiplier

        p1_wins += p1_w * p1_multiplier

    p1_round = p1_aggregated

    p1_outcomes = 0
    for e in p1_round.keys():
        p1_outcomes += p1_round[e]

    print(
        "P1: Round %s, Input %s scenarios, Won in %s outcomes, Other outcomes %s"
        % (i, p1_count, p1_wins, p1_outcomes)
    )

    p2_count = 0

    for p2_nextstep in p2_round.keys():

        p2_multiplier = p2_round[p2_nextstep]
        p2_count += p2_multiplier

        p2_oc, p2_w = round(p2_nextstep)

        for p2_outcome in p2_oc:
            if p2_outcome in p2_aggregated:
                p2_aggregated[p2_outcome] += p2_multiplier
            else:
                p2_aggregated[p2_outcome] = p2_multiplier

        p2_wins += p2_w * p2_multiplier

    p2_round = p2_aggregated

    p2_outcomes = 0
    for e in p2_round.keys():
        p2_outcomes += p2_round[e]

    print(
        "P2: Round %s, Input %s scenarios, Won in %s outcomes, Other outcomes %s"
        % (i, p2_count, p2_wins, p2_outcomes)
    )

    p1_tot_wins += p1_wins * p2_count
    p2_tot_wins += p2_wins * p1_outcomes


print(
    "P1 total winning outcomes %s, P2 total winning outcomes %s"
    % (p1_tot_wins, p2_tot_wins)
)
