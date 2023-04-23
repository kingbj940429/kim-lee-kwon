# 문제이해, 접근방식, 코드설계, 코드구현

# 걍 다 어피치가 유리함
# 라이언이 이길 수 없는 경우 -1

from collections import defaultdict
from itertools import combinations_with_replacement

from collections import defaultdict
from itertools import combinations_with_replacement

def solution(n, info):
    answer = []
    score = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    abs_score = 0;
    case1 = list(combinations_with_replacement(score, n))
    case2 = []

    for c in case1:
        s = [0 for _ in range(11)]
        for l in list(c):
            s[10-l] += 1
        case2.append(s)

    for c in case2:
        s1, s2 = 0, 0
        for i in range(11):
            if info[i] > 0 or c[i] > 0:
                if info[i] < c[i]:
                    s2 += 10-i
                else:
                    s1 += 10-i
        if s2 > s1:
            if (s2 - s1) > abs_score:
                abs_score = (s2 - s1)
                answer = [c]
            if (s2 - s1) == abs_score:
                answer.append(c)
    answer.sort(key=lambda x:(-x[10], -x[9], -x[8], -x[7], -x[6], -x[5], -x[4], -x[3], -x[2], -x[1], -x[0]))
    return answer[0] if len(answer) > 0 else [-1]


# def solution(n, infos):
#     answer = []
#     max_scores = [0]
#     coverage = range(10,0,-1)
#
#     combs = list(combinations_with_replacement(coverage, n))
#     apeach = to_dict_apeach(infos)
#
#     for com in combs:
#         high_scores = [0] * 11
#         ryan = to_dict_ryan(com)
#
#         apeach_score = 0
#         ryan_score = 0
#
#         for i in range(0, 11):
#             if apeach[10 - i] >= ryan[10 - i] and apeach[10 - i] != 0:
#                 apeach_score += 10 - i
#             elif ryan[10 - i] > apeach[10 - i] and ryan[10 - i] != 0:
#                 ryan_score += 10 - i
#
#         if ryan_score > apeach_score:
#             max_scores.append(ryan_score)
#             for key, value in ryan.items():
#                 high_scores[10-key] = value
#
#             answer.append(high_scores)
#
#     if not answer:
#         return [-1]
#
#     max_score = max(max_scores)
#     max_scores = []
#
#     for ans in answer:
#         temp = 0
#
#         for i, v in enumerate(ans):
#             if v != 0:
#                 temp += 10-i
#
#         if temp == max_score:
#             max_scores.append(ans)
#
#     max_scores.sort(key=lambda x:(-x[10], -x[9], -x[8], -x[7], -x[6], -x[5], -x[4], -x[3], -x[2], -x[1], -x[0]))
#
#     return max_scores[0]

def to_dict_apeach(arrows):
    result = defaultdict(int)

    for i in range(0, 11):
        result[10-i] = arrows[i]

    return result

def to_dict_ryan(arrows):
    result = defaultdict(int)

    for i in range(0, 11):
        result[10-i] = arrows.count(10-i)

    return result


if __name__=="__main__":
    # n = 5
    # info =[2,1,1,1,0,0,0,0,0,0,0]
    n = 9
    info = [0,0,1,2,0,1,1,1,1,1,1]

    print(solution(n, info)) # [0,2,2,0,1,0,0,0,0,0,0]