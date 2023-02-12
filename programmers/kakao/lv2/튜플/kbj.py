# 문제이해, 접근방식, 코드설계, 코드구현
# 조건
# 숫자가 0으로 시작하는 경우는 없습니다.
# s는 항상 중복되는 원소가 없는 튜플을 올바르게 표현하고 있습니다.

# s 길이가 최대 10^6 이므로 O(n^2) 일 경우 시간초과 가능성있음
def solution(s):
    answer = []

    s = s[2:-2].split("},{")
    s.sort(key=lambda x: len(x))

    for c in s:
        csv_arr = list(map(int, c.split(",")))
        for c2 in csv_arr:
            if c2 not in answer:
                answer.append(c2)

    return answer

if __name__=="__main__":
    s = "{{1,2,3},{2,1},{1,2,4,3},{2}}" # [2, 1, 3, 4]
    print(solution(s))