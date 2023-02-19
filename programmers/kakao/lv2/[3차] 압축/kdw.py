def solution(msg):
    answer = []

    k = ord('A') - 1
    dic = {chr(i + k): i for i in range(1, 27)}

    msg += ' '
    n = len(msg)
    i = 0
    while i < n - 1:
        w = msg[i]
        for j in range(i + 1, n):
            c = msg[j]
            if w in dic and w + c not in dic:
                answer.append(dic[w])
                dic[w + c] = len(dic) + 1
                break
            w += c
        i = j

    return answer
