from collections import defaultdict
from itertools import combinations
from bisect import bisect_left


def solution(info, query):
    answer = []
    group = defaultdict(list)

    for *application, score in map(lambda x: x.split(), info):
        score = int(score)
        for r in range(5):
            for comb in combinations(application, r):
                group[''.join(comb)].append(score)

    for scores in group.values():
        scores.sort()

    for *application, score in map(lambda x: x.replace('and', '').replace('-', '').split(), query):
        application = ''.join(application)
        idx = bisect_left(group[application], int(score))
        answer.append(len(group[application]) - idx)

    return answer
