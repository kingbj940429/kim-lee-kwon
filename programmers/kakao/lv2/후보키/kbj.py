# 문제이해 > 접근방식 > 코드설계 > 코드구현

def checkUnique(relation, columns, head):
    result = []
    uniqueCheck = {}
    for v in relation:
        STR = '-'.join([item for i, item in enumerate(v) if i in columns ])
        uniqueCheck[STR] = 0

    if len(uniqueCheck) == len(relation):
        result.append(columns)

    for v in range(head+1, len(relation[0])):
        result += checkUnique(relation, columns + [v], v)

    return result

def solution(relation):
    answer = checkUnique(relation, [], -1)
    ans = []
    for i in range(0, len(answer)):
        cnt = 0
        for j in range(0, len(answer)):
            if set(answer[i]) > set(answer[j]):
                cnt += 1
        if cnt == 0:
            ans.append(answer[i])
    return len(ans)

if __name__ == "__main__":
    relation = [
                ["100", "ryan", "music", "2"],
                ["200", "apeach", "math", "2"],
                ["300", "tube", "computer", "3"],
                ["400", "con", "computer", "4"],
                ["500", "muzi", "music", "3"],
                ["600", "apeach", "music", "2"]
                ]

    print(solution(relation)) # 2