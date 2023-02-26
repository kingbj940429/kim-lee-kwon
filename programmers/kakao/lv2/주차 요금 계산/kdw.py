from collections import defaultdict


def solution(fees, records):
    answer = []

    total = defaultdict(int)
    parking = {}

    for r in records:
        time, car, side = r.split()
        hours, mins = map(int, time.split(':'))
        mins += hours * 60
        if side == 'IN':
            parking[car] = mins
        else:
            total[car] += mins - parking.pop(car)

    for car, mins in parking.items():
        total[car] += 1439 - mins

    for _, mins in sorted(total.items()):
        if mins > fees[0]:
            div, mod = divmod(mins - fees[0], fees[2])
            if mod:
                div += 1
            answer.append(fees[1] + div * fees[3])
        else:
            answer.append(fees[1])

    return answer
