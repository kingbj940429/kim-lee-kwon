from itertools import combinations
from collections import defaultdict


def solution(orders, course):
    answer = []
    orders = list(map(sorted, orders))

    for r in course:
        dic = defaultdict(int)
        for order in orders:
            for comb in combinations(order, r):
                dic[comb] += 1
        if dic:
            max_val = max(dic.values())
            if max_val > 1:
                answer += list(filter(lambda x: dic[x] == max_val, dic))

    return sorted(map(''.join, answer))
