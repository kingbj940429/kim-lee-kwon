from itertools import product
from collections import defaultdict

def solution(users, emoticons):
    answer = []

    discounted_emotions = emoticons_discounted(emoticons)

    for emo in discounted_emotions:
        plus_service = 0
        total_price = 0

        for user in users:
            discount, max_price = user
            price = 0 # max_price 와 비교하기 위한 가격

            for key in emo.keys(): # 할인 이모티콘 딕셔너리
                if discount <= key:
                    price += sum([int((v * (100 - key) / 100)) for v in emo[key]]) # 할인 받는 구간의 가격 합

            if price >= max_price:
                plus_service += 1
            else:
                total_price += price
        answer.append([plus_service, total_price])

    return sorted(answer, key=lambda x: (x[0],x[1]), reverse=True)[0]

def emoticons_discounted(emoticons):
    discount = [10, 20, 30, 40]
    result = []

    for coms in product(discount, repeat = len(emoticons)):
        dic = defaultdict(list)
        for com, emo in zip(coms, emoticons):
            dic[com].append(emo)

        result.append(dic)

    return result


if __name__=="__main__":
    users = [[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]]
    emoticons = [1300, 1500, 1600, 4900]

    # users = [[40, 10000], [25, 10000]]
    # emoticons = [7000, 9000]


    print(solution(users, emoticons)) # [4, 13860], [1, 5400]