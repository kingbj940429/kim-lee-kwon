# 문제이해 > 접근방식 > 코드설계 > 코드구현

# 조건
# 큐 합 같게 못하면 > -1

# 시간복잡도
# worst case 가 10^5 정도?

from collections import deque

def solution(queue1, queue2):
    deq1 = deque(queue1)
    deq2 = deque(queue2)
    sum_deq1 = sum(deq1)
    sum_deq2 = sum(deq2)

    goal = int((sum_deq1 + sum_deq2)/2)

    # 홀수이면 바로 리턴
    if (sum_deq1 + sum_deq2) % 2 != 0:
        return -1

    # goal 보다 큰 원소가 있어도 바로 리턴
    if max(deq1) > goal or max(deq2) > goal:
        return -1

    for i in range(300000):
        if sum_deq1 < sum_deq2:
            pop = deq2.popleft()
            deq1.append(pop)

            sum_deq1 += pop
            sum_deq2 -= pop

        elif sum_deq1 > sum_deq2:
            pop = deq1.popleft()
            deq2.append(pop)

            sum_deq2 += pop
            sum_deq1 -= pop

        else:
            return i
    return -1

if __name__=="__main__":
    queue1 = [3, 2, 7, 2]
    queue2 = [4, 6, 5, 1]
    # queue1 = [1, 1]
    # queue2 = [1, 5]

    print(solution(queue1, queue2))