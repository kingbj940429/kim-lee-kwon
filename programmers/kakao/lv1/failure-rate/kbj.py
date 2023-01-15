from collections import Counter

def solution(N, stages):
    answer = {}
    lentgh = len(stages)
    counter = Counter(stages)    

    for i in range(1, N+1):
        if lentgh:
            fail_cnt = counter[i]
            answer[i] = (float(fail_cnt)/float(lentgh))

            lentgh -= fail_cnt
        else:
            answer[i] = 0

    return sorted(answer, key=lambda x: answer[x], reverse=True)

if __name__=="__main__":
    N = 5
    stages = [2, 1, 2, 6, 2, 4, 3, 3]	
    print(solution(N, stages))