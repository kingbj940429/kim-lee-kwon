from collections import defaultdict


def solution(id_list, report, k):
    dic1 = defaultdict(set)
    for r in report:
        a, b = r.split()
        dic1[b].add(a)

    dic2 = defaultdict(int)
    for v in dic1.values():
        if len(v) >= k:
            for a in v:
                dic2[a] += 1

    return [*map(lambda x: dic2[x], id_list)]


'''
from collections import defaultdict


def solution(id_list, report, k):
    report = set(report)

    dic1 = defaultdict(int)
    for r in report:
        dic1[r.split()[1]] += 1

    dic2 = defaultdict(int)
    for r in report:
        a, b = r.split()
        if dic1[b] >= k:
            dic2[a] += 1

    return [*map(lambda x: dic2[x], id_list)]
'''
