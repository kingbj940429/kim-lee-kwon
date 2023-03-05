# 문제이해, 접근방식, 코드설계, 코드구현
# 조건
# 1. 차량 번호가 작은 자동차 순
# 2. 나누어 떨어지지 않으면 올림
# 3. 당일 입출차만 신경 쓰면됨
# 4. 출차 없으면 23:59

# 시간 복잡도
# records 의 길이가 1000 이므로 신경 안써도 될듯

# ---------------------------------------

from math import ceil
from collections import defaultdict
def solution(fees, records):
    answer = []
    cars_parked = defaultdict(int)
    total_mins = defaultdict(int)

    for record in records:
        time, car_num, way = record.split(" ")

        if way == "IN":
            cars_parked[car_num] = time
        elif way == "OUT":
            total_min = to_min(time) - to_min(cars_parked[car_num])
            cars_parked[car_num] = 0
            total_mins[car_num] += total_min

    # 출차 흔적이 없을 경우
    for car_num, time in cars_parked.items():
        if time != 0:
            total_min = to_min("23:59") - to_min(cars_parked[car_num])
            total_mins[car_num] += total_min

    for i in sorted(calculate_fee(fees, total_mins), key=lambda x: x[0]):
        answer.append(i[1])

    return answer

def to_min(time):
    hour, min = time.split(":")

    return int(hour) * 60 + int(min)

def calculate_fee(fees, total_mins) :
    time, fee, per_min, per_won = int(fees[0]), int(fees[1]), int(fees[2]), int(fees[3])

    results = []

    for car_num, min in total_mins.items():
        if time < min:
            results.append([car_num, fee + ceil((min - time)/per_min) * per_won])
        else:
            results.append([car_num, fee])

    return results


if __name__ == "__main__":
    fees = [180, 5000, 10, 600] # 기본시간(분), 기본요금(원), 단위시간(분), 단위요금(원)
    records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]

    result = solution(fees, records)

    print(result) # [14600, 34400, 5000]