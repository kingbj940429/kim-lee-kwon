# 문제이해 > 접근방식 > 코드설계 > 코드구현

# 조건
# - 최소 2명 이상의 손님으로부터의 주문메뉴
# - 결과는 오름차순

# 시간복잡도 - 매우 작아서 신경 안씀

import collections
import itertools

def solution(orders, course):
    result = []

    for course_size in course:
        order_combinations = []
        for order in orders:
            order_combinations += itertools.combinations(sorted(order), course_size)

        most_ordered = collections.Counter(order_combinations).most_common()
        print(most_ordered)
        result += [ k for k, v in most_ordered if v > 1 and v == most_ordered[0][1] ]

    return [ ''.join(v) for v in sorted(result) ]

# def solution(orders, course):
#     answer = []
#
#     for size_of_course in course:
#         order_dict = {}
#         order_combinations = []
#         for order in orders:
#             order_combinations.extend(list(itertools.combinations(sorted(order), size_of_course)))
#
#         for order_combination in order_combinations:
#             order_str = ''.join(order_combination)
#             if order_str in order_dict:
#                 order_dict[order_str] += 1
#             else:
#                 order_dict[order_str] = 1
#
#         for order in order_dict:
#             if order_dict[order] == max([order_dict[order] for order in order_dict]):
#                 if order_dict[order] > 1:
#                     answer.append(order)
#
#     return sorted(answer)

if __name__=="__main__":
    orders = ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"]
    course = [2,3,5] # ["AC", "ACDE", "BCFG", "CDE"]

    print(solution(orders, course))