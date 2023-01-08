def solution(dartResult):
    answer = []

    for s in dartResult.replace('10', 'A'):
        if s == 'S':
            continue
        elif s == 'D':
            answer[-1] **= 2
        elif s == 'T':
            answer[-1] **= 3
        elif s == '*':
            answer[-1] *= 2
            if len(answer) > 1:
                answer[-2] *= 2
        elif s == '#':
            answer[-1] *= -1
        elif s == 'A':
            answer.append(10)
        else:
            answer.append(int(s))

    return sum(answer)
