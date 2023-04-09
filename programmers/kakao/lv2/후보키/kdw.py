from itertools import combinations


def solution(relation):
    candidates = []
    row_size = len(relation)
    rows = range(len(relation))
    cols = range(len(relation[0]))

    for k in cols:
        for comb in combinations(cols, k + 1):
            if len({tuple(relation[r][c] for c in comb) for r in rows}) == row_size:
                set_comb = set(comb)
                for candidate in candidates:
                    if set_comb.issuperset(candidate):
                        break
                else:
                    candidates.append(comb)

    return len(candidates)
