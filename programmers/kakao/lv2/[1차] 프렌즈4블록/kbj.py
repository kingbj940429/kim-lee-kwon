# 문제이해 > 접근방식 > 코드설계 > 코드구현

# 시간복잡도
# 딱히 생각안해도 될 듯

def solution(m, n, board):
    for i in range(m):
        board[i] = list(board[i])

    cnt = 0
    rm = set()
    while True:
        for i in range(m - 1):
            for j in range(n - 1):
                t = board[i][j]
                if t == []:
                    continue
                if board[i + 1][j] == t and board[i][j + 1] == t and board[i + 1][j + 1] == t:
                    rm.add((i, j))
                    rm.add((i + 1, j))
                    rm.add((i, j + 1))
                    rm.add((i + 1, j + 1))

        if rm:
            cnt += len(rm)
            for i, j in rm:
                board[i][j] = []
            rm = set()
        else:
            return cnt

        while True:
            moved = 0
            for i in range(m - 1):
                for j in range(n):
                    if board[i][j] and board[i + 1][j] == []:
                        board[i + 1][j] = board[i][j]
                        board[i][j] = []
                        moved = 1
            if moved == 0:
                break


if __name__=="__main__":
    m, n, board = 4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"]
    solution(m, n, board)