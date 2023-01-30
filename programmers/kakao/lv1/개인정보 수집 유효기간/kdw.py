def to_int(date):
    YYYY, MM, DD = map(int, date.split('.'))
    MM, DD = MM - 1, DD - 1
    return (YYYY * 12 + MM) * 28 + DD


# for test
def to_str(date):
    DD = date % 28
    YYYY, MM = divmod(date // 28, 12)
    MM, DD = MM + 1, DD + 1
    return str(YYYY) + '.' + str(MM) + '.' + str(DD)


def solution(today, terms, privacies):
    answer = []

    dic = {}
    for t in terms:
        k, v = t.split()
        dic[k] = int(v)

    today = to_int(today)

    for i, p in enumerate(privacies, 1):
        date, k = p.split()
        if today >= to_int(date) + dic[k] * 28:
            answer.append(i)

    return answer


'''
def solution(today, terms, privacies):
    answer = []

    dic = {}
    for t in terms:
        k, v = t.split()
        dic[k] = int(v)

    ty, tm, td = map(int, today.split('.'))

    for i, p in enumerate(privacies, 1):
        date, k = p.split()
        y, m, d = map(int, date.split('.'))
        m += dic[k]
        if m > 12:
            m -= 1
            y += m // 12
            m %= 12
            m += 1
        if (ty > y
            or ty == y and tm > m
            or ty == y and tm == m and td >= d):
            answer.append(i)

    return answer
'''
