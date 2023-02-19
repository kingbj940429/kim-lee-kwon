# 문제이해, 접근방식, 코드설계, 코드구현

# 조건
# 최대 10^6 이므로 O(n^2) 가능
# 영문자만 가능
# 대소문자 구분 안함
# 다중집합
from collections import deque
def solution(str1, str2):
    str1, str2 = str1.lower(), str2.lower()

    str1 = to_pair_list(str1)
    str2 = to_pair_list(str2)


    common_similarity = len(to_multiple_common(str1, str2))
    sum_similarity = len(to_multiple_sum(str1, str2))

    if common_similarity == 0 and sum_similarity == 0:
        return int(65536)
    else:
        return int(common_similarity/sum_similarity * 65536)

def to_pair_list(str):
    results = []

    for i in range(len(str)-1):
        if str[i:i+2].isalpha():
            results.append(str[i:i+2])

    return results

def to_multiple_common(str1, str2):
    multiple_common = []

    str1_deq = deque(str1)
    str2_deq = deque(str2)

    for ch in str1_deq:
        if ch in str2_deq:
            str2_deq.remove(ch)
            multiple_common.append(ch)

    return multiple_common


def to_multiple_sum(str1, str2):
    str1_deq = deque(str1)
    str2_deq = deque(str2)
    str2_deq_temp = deque(str2)

    for ch in str1_deq:
        if ch not in str2_deq_temp:
            str2_deq.append(ch)
        else:
            str2_deq_temp.remove(ch)

    return str2_deq

if __name__=="__main__":
    str1 = "E=M*C^2"
    str2 = "e=m*c^2"

    # 16384
    print(solution(str1, str2))