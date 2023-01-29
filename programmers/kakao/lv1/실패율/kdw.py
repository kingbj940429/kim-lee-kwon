from collections import Counter


def solution(N, stages):
    answer = {}
    length = len(stages)
    counter = Counter(stages)

    for i in range(1, N + 1):
        if length:
            answer[i] = counter[i] / length
            length -= counter[i]
        else:
            answer[i] = 0

    return sorted(answer,
                  key=lambda x: answer[x],
                  reverse=True)
