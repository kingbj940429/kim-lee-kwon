from itertools import combinations_with_replacement


def solution(n, info):
    answer = [-1]
    difference = 0

    for arrows in combinations_with_replacement(range(11), n):
        target = [0 for _ in range(11)]
        for arrow in arrows:
            target[10 - arrow] += 1

        ryan = apeach = 0
        for i, (a, b) in enumerate(zip(info, target)):
            if a == b == 0:
                continue
            elif a < b:
                ryan += 10 - i
            else:
                apeach += 10 - i

        if difference < ryan - apeach:
            answer = target
            difference = ryan - apeach

    return answer
