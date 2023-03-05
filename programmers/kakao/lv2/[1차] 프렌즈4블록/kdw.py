def find(m, n, board):
    found = set()
    for r in range(m - 1):
        for c in range(n - 1):
            if not board[r][c]:
                continue
            if board[r][c] == board[r][c + 1] == board[r + 1][c] == board[r + 1][c + 1]:
                found.update({(r, c), (r, c + 1), (r + 1, c), (r + 1, c + 1)})
    return found


def erase(m, n, board, found):
    for r, c in found:
        board[r][c] = None
    for c in range(n):
        nr = m - 1
        for r in range(m - 1, -1, -1):
            if (r, c) not in found:
                board[nr][c] = board[r][c]
                nr -= 1


def solution(m, n, board):
    answer = 0
    board = list(map(list, board))
    while True:
        found = find(m, n, board)
        if not found:
            break
        answer += len(found)
        erase(m, n, board, found)
    return answer
