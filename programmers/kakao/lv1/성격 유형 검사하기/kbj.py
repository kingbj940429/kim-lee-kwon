# 문제 이해, 접근 방식, 코드 설계, 코드 구현
# Big-O() : survey 에 따라 시간 복잡도가 달라짐
# 구현문제
# 두 성격 유형 중 사전 순으로 빠른 성격 유형을 검사자의 성격 유형이라고 판단합니다.
def solution(survey, choices):
    answer = ''
    scores = [3,2,1,0,1,2,3]
    results = {"R": 0,"T": 0,"C": 0,"F": 0,"J": 0,"M": 0,"A": 0,"N": 0}

    for sur,choice in zip(survey, choices):
        first = sur[0]
        second = sur[1]

        if choice > 4:
            results[second] += scores[choice-1]
        else:
            results[first] += scores[choice-1]

    return to_MBTI(results)

def to_MBTI(results):

    return (("T" if results["T"] > results["R"] else "R") +
            ("F" if results["F"] > results["C"] else "C") +
            ("M" if results["M"] > results["J"] else "J") +
            ("N" if results["N"] > results["A"] else "A"))



if __name__=="__main__":
    survey = ["TR", "RT", "TR"]
    choices = [7, 1, 3]
    # "RCJA"
    print(solution(survey, choices))