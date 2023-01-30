def solution(numbers, hand):
    answer = [None for _ in range(len(numbers))]
    loc = [(3, 1),
           (0, 0), (0, 1), (0, 2),
           (1, 0), (1, 1), (1, 2),
           (2, 0), (2, 1), (2, 2),
           (3, 0), (3, 2)]
    l, r = 10, 11
    left_side, right_side = {1, 4, 7}, {3, 6, 9}
    left_handed = True if hand[0] == 'l' else False

    for i, num in enumerate(numbers):
        if num in left_side:
            answer[i], l = 'L', num
        elif num in right_side:
            answer[i], r = 'R', num
        else:
            ld = abs(loc[num][0] - loc[l][0]) + abs(loc[num][1] - loc[l][1])
            rd = abs(loc[num][0] - loc[r][0]) + abs(loc[num][1] - loc[r][1])
            if ld < rd or ld == rd and left_handed:
                answer[i], l = 'L', num
            else:
                answer[i], r = 'R', num

    return ''.join(answer)
