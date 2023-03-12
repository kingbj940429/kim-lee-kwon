# 문제이해, 접근방식, 코드설계, 코드구현

# 조건
# 1. 중복은 가능하나 누군지 구별 필요
# 2. 나갔다 닉네임 변경 후 들어오면 이전꺼 다 변경

# 시간 복잡도
# 100,000 이므로 n^2 는 안될 수도

from collections import defaultdict
def solution(record):
    answer = []
    record = [r.split(" ") for r in record]
    dic_record = to_dict(record)

    for r in record:
        way, uid = r[0], r[1]

        if way == "Enter" or way == "Change":
            dic_record[uid] = r[2]

    for r in record:
        way, uid = r[0], r[1]

        if way == "Enter":
            answer.append(dic_record[uid] + "님이 들어왔습니다.")
        elif way == "Leave":
            answer.append(dic_record[uid] + "님이 나갔습니다.")

    return answer

def to_dict(record):
    dic_record = defaultdict(str)

    for r in record:
        way, uid = r[0], r[1]

        if way != "Leave":
            dic_record[uid] = r[2]

    return dic_record


if __name__ == "__main__":
    record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]

    answer = solution(record)

    print(answer) # ["Prodo님이 들어왔습니다.", "Ryan님이 들어왔습니다.", "Prodo님이 나갔습니다.", "Prodo님이 들어왔습니다."]