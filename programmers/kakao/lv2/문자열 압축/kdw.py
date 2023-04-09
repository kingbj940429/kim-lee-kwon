def compress(s, length, unit):
    expression = []
    previous = s[:unit]
    repeat = 0

    for i in range(unit, length + unit, unit):
        current = s[i:i + unit]
        if current == previous:
            repeat += 1
        else:
            if repeat:
                previous = str(repeat + 1) + previous
            expression += previous
            repeat = 0
        previous = current

    return ''.join(expression)


def solution(s):
    answer = length = len(s)

    for unit in range(1, length // 2 + 1):
        expression = compress(s, length, unit)
        answer = min(answer, len(expression))

    return answer
