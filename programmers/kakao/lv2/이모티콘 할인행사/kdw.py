from itertools import product


def solution(users, emoticons):
    answer = [0, 0]

    for discount_rates in product([10, 20, 30, 40], repeat=len(emoticons)):
        subscriber, sales_amount = 0, 0
        for user_rate, user_price in users:
            purchase_cost = 0
            for discount_rate, emoticon_price in zip(discount_rates, emoticons):
                if discount_rate >= user_rate:
                    purchase_cost += emoticon_price * (100 - discount_rate) // 100
            if purchase_cost >= user_price:
                subscriber += 1
            else:
                sales_amount += purchase_cost
        answer = max(answer, [subscriber, sales_amount])

    return answer
