from collections import Counter


def solution(s):
    nums = s.replace('{', '').replace('}', '').split(',')
    return [int(x[0]) for x in sorted(Counter(nums).items(),
                                      key=lambda x: x[1],
                                      reverse=True)]


'''
def solution(s):
    answer = []

    s = sorted(set(x.split(',')) for x in s[2:-2].split('},{'))
    px = set()

    for x in s:
        dx = (x - px).pop()
        answer.append(int(dx))
        px = x

    return answer
'''
