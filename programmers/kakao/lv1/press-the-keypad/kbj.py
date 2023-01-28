def solution(numbers, hand):
    answer = ''
    left = [1, 4, 7]
    middle = [2, 5, 8, 0]
    right = [3, 6, 9]

    last_left_pos = [0, 3]
    last_right_pos = [2, 3]

    for i, val in enumerate(numbers):
        if val in left:
            answer += "L"
            last_left_pos[0] = 0
            last_left_pos[1] = left.index(val)
        elif val in right:
            answer += "R"
            last_right_pos[0] = 2
            last_right_pos[1] = right.index(val)
        else:
            left_diff_w = abs(1 - last_left_pos[0])
            left_diff_h = abs(middle.index(val) - last_left_pos[1])
            left_diff = left_diff_w + left_diff_h

            right_diff_w = abs(1 - last_right_pos[0])
            right_diff_h = abs(middle.index(val) - last_right_pos[1])
            right_diff = right_diff_w + right_diff_h

            if left_diff > right_diff:
                answer += "R"
            elif right_diff > left_diff:
                answer += "L"
            elif left_diff == right_diff:
                if hand == "right":
                    answer += "R"
                else:
                    answer += "L"

            if answer[-1] == "L":
                last_left_pos[0] = 1
                last_left_pos[1] = middle.index(val)
            else:
                last_right_pos[0] = 1
                last_right_pos[1] = middle.index(val)

    return answer