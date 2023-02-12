# https://docs.python.org/ko/3/library/collections.html
from collections import Counter


def solution(str1, str2):
    A = Counter(str1[i:i+2].lower() for i in range(len(str1) - 1) if str1[i:i+2].isalpha())
    B = Counter(str2[i:i+2].lower() for i in range(len(str2) - 1) if str2[i:i+2].isalpha())
    AnB, AUB = (A & B).values(), (A | B).values()
    return int(sum(AnB) / sum(AUB) * 65536) if AUB else 65536


'''
from collections import defaultdict


def solution(str1, str2):
    dic1, dic2 = defaultdict(int), defaultdict(int)
    str1, str2 = str1.lower(), str2.lower()

    for i in range(len(str1) - 1):
        if 'a' <= str1[i] <= 'z' and 'a' <= str1[i + 1] <= 'z':
            dic1[str1[i] + str1[i + 1]] += 1

    for i in range(len(str2) - 1):
        if 'a' <= str2[i] <= 'z' and 'a' <= str2[i + 1] <= 'z':
            dic2[str2[i] + str2[i + 1]] += 1

    intersection = union = 0

    for k in dic1:
        if k in dic2:
            intersection += min(dic1[k], dic2[k])
            union += max(dic1[k], dic2[k])
        else:
            union += dic1[k]

    for k in dic2:
        if k not in dic1:
            union += dic2[k]

    return int(intersection / union * 65536) if union else 65536
'''
