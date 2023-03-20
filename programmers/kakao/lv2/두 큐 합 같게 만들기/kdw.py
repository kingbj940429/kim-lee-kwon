def solution(queue1, queue2):
    answer = 0
    queue = queue1 + queue2 + queue1
    end = len(queue)
    left, right = 0, len(queue1) - 1
    sum1 = sum(queue1)
    half = (sum1 + sum(queue2)) // 2

    while left <= right:
        if sum1 == half:
            return answer
        if sum1 > half:
            sum1 -= queue[left]
            left += 1
        else:
            right += 1
            if right == end:
                return -1
            sum1 += queue[right]
        answer += 1
    return -1


print(solution([1, 2, 9, 4], [1, 1, 2, 2]))  # 8
print(solution([1, 10, 1, 2], [1, 2, 1, 2]))  # 7
