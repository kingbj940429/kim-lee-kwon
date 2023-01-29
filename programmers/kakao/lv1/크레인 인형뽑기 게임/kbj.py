# 문제 이해하기, 접근 방식, 코드 설계, 코드 구현
# Bio-O(N^2)
def solution(board, moves):
    answer = 0
    N = len(board)
    bucket = [0]

    for move in moves:
        for i in range(0,N):
            if board[i][move-1] != 0:
                obj = board[i][move-1]
                answer += checkBucket(bucket, obj)

                board[i][move - 1] = 0
                break

    return answer

def checkBucket(bucket, new):
    if bucket[-1] == new:
        bucket.pop()
        return 2
    else:
        bucket.append(new)
        return 0


if __name__ == "__main__":
    board = [[0,0,0,0,0],
             [0,0,1,0,3],
             [0,2,5,0,1],
             [4,2,4,4,2],
             [3,5,1,3,1]]

    moves = [1,5,3,5,1,2,1,4]

    print(solution(board, moves))