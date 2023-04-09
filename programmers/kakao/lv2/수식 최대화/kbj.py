# 문제이해 > 접근방식 > 코드설계 > 코드구현

# 조건
# 1. 동일한 연산 순위 없음
# 2. 음수 일경우 절대값으로 변환
# 3. 가장 큰 참가자가 우승

# 시간복잡도 -> 최대 길이 10^2 , 연산 최대 조합은 6개이므로 시긴복잡도 생각은 크게 신경쓸 필요 없음

import itertools
def solution(expression):
    answer = list(itertools.permutations(["*","-","+"],3))
    n=""
    num = []
    x = []
    for i in expression:
        if(i=="*" or i=="-" or i=="+"):
            x.append(i)
            num.append(n)
            n=""
            continue
        n += i
    else:
        num.append(n)

    num2=list(num)
    x2=list(x)
    a=[]
    for i in answer:
        x = list(x2)
        num = list(num2)
        for j in i:
            while (True):
                if (j in x):
                    num[x.index(j)] = str(eval(num[x.index(j)] + j + num[x.index(j) + 1]))
                    num.pop(x.index(j) + 1)
                    x.pop(x.index(j))
                else:
                    break
        a.append(abs(int(num[0])))
    return max(a)



if __name__ == "__main__":
    string = "100-200*300-500+20"
    result = solution(string)

    print(result)