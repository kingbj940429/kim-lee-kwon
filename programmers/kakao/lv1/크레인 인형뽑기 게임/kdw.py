def solution(board, moves):
    answer = 0

    N = len(board)
    dolls = [[] for _ in range(N)]
    for i in range(N):
        for j in range(N - 1, -1, -1):
            if not board[j][i]:
                break
            dolls[i].append(board[j][i])
    dolls.insert(0, [])

    basket = [0]
    for i in moves:
        if dolls[i]:
            x = dolls[i].pop()
            if basket[-1] == x:
                basket.pop()
                answer += 2
            else:
                basket.append(x)

    return answer
