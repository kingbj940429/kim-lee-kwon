# 문제이해, 접근방식, 코드설계, 코드구현
# O(n^2) 이여도 최대가 10^4 이므로 상관없을듯
# 모든 달은 28일
def solution(today, terms, privacies):
    answer = []
    terms_dict = {v.split(" ")[0]:v.split(" ")[1] for v in terms}
    today_days = int(today.split(".")[0]) * 28 * 12 + int(today.split(".")[1]) * 28 + int(today.split(".")[2])

    for i,privacy in enumerate(privacies):
        created_at = privacy.split(" ")[0]
        term = privacy.split(" ")[1]

        privacy_days = int(created_at.split(".")[0]) * 28 * 12 + int(created_at.split(".")[1]) * 28 + int(created_at.split(".")[2])

        if today_days >= privacy_days + int(terms_dict[term]) * 28:
            answer.append(i+1)

    return answer

if __name__=="__main__":
    today = "2020.01.01"
    terms = ["Z 3", "D 5"]
    privacies = ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"]

    print(solution(today, terms, privacies))
