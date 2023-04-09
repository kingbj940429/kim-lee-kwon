# 문제이해 > 접근방식 > 코드설계 > 코드구현

# 조건
# 거리두기 지키면 1, 한 명이라도 아니면 0

from collections import deque

def solution(places):
    answer = []

    for place in places:
        matrix = to_matrix(place)
        break_flag = False

        # 하나의 매트릭
        for i in range(len(matrix)):
            # 매트릭 한줄
            for j in range(len(matrix[i])):

                if matrix[i][j] == 'P':
                    up, down, left, right = matrix[i-1][j], matrix[i+1][j], matrix[i][j-1], matrix[i][j+1]
                    o_up, o_down, o_left, o_right = 'X', 'X', 'X', 'X'

                    # O 인 경우
                    if up == 'O':
                        o_left = matrix[i - 1][j - 1]
                        o_right = matrix[i - 1][j + 1]
                        o_up = matrix[i - 2][j]
                    elif down == 'O':
                        o_left = matrix[i + 1][j - 1]
                        o_right = matrix[i + 1][j + 1]
                        o_down = matrix[i + 2][j]
                    elif left == 'O':
                        o_up = matrix[i - 1][j - 1]
                        o_down = matrix[i + 1][j - 1]
                        o_left = matrix[i][j - 2]
                    elif right == 'O':
                        o_up = matrix[i - 1][j + 1]
                        o_down = matrix[i + 1][j + 1]
                        o_right = matrix[i][j + 2]

                    # 상하좌우 P 가 있는지 확인 -> 바로 0 리턴
                    if up == 'P' or down == 'P' or left == 'P' or right == 'P' or o_left == 'P' or o_right == 'P' or o_up == 'P' or o_down == 'P':
                        answer.append(0)
                        break_flag = True
                        break
            if break_flag:
                break

        if break_flag:
            continue
        else:
            answer.append(1)

    return answer

def to_matrix(place):
    matrix = deque([])
    matrix.appendleft(['X','X','X','X','X','X','X','X','X'])
    matrix.appendleft(['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'])

    for row in place:
        row = 'XX' + row + 'XX'
        matrix.append(list(row))

    matrix.append(['X','X','X','X','X','X','X','X','X'])
    matrix.append(['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'])
    return list(matrix)

if __name__ == "__main__":
    places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
    print(solution(places)) # [1, 0, 1, 1, 1]