def solution(record):
    log, dic = [], {}

    for r in record:
        r = r.split()
        if r[0] == 'Enter':
            dic[r[1]] = r[2]
            log.append((r[1], '님이 들어왔습니다.'))
        elif r[0] == 'Leave':
            log.append((r[1], '님이 나갔습니다.'))
        else:
            dic[r[1]] = r[2]

    return [*map(lambda x: dic[x[0]] + x[1], log)]
