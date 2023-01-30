from collections import defaultdict


def solution(survey, choices):
    dic = defaultdict(int)
    for s, c in zip(survey, choices):
        dic[s[c // 4]] += abs(c - 4)

    return (('T' if dic['T'] > dic['R'] else 'R') +
            ('F' if dic['F'] > dic['C'] else 'C') +
            ('M' if dic['M'] > dic['J'] else 'J') +
            ('N' if dic['N'] > dic['A'] else 'A'))
