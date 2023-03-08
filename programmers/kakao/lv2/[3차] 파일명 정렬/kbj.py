# 문제이해, 접근방식, 코드설계, 코드구현

# 조건
# 1. HEAD 는 대소문자 구분 X, 문자만
# 2. NUMBER 는 1~5 글, 앞에 0이 올 수 있음
# 3. TAIL 은 빈 문자열일 수 있고, 숫자랑 문자가 섞임
# 4. HEAD 부분과, NUMBER의 숫자도 같을 경우, 그냥 들어오는 순서대로
# 5. 0 의 갯수만 다른 중복된 텍스트가 있을 수 있음

# 시간복잡도
# files 가 최대 1000개이므로 n^2 가능

import re

def solution(files):
    a = sorted(files, key=lambda file : int(re.findall('\d+', file)[0]))
    b = sorted(a, key=lambda file : re.split('\d+', file.lower())[0])
    return b

# def solution(files):
#     files_divided = split_files(files)
#     print(files_divided)
#     files_sorted = sorted(files_divided, key=lambda x: (x[0].lower(), int(x[1])))
#
#     return ["".join(file) for file in files_sorted]
#
# def split_files(files):
#     result = []
#
#     for file in files:
#         head_flag, number_flag = False, False
#         head, number, tail = "", "", ""
#
#         for c in file:
#             # HEAD
#             if not c.isdigit() and not head_flag:
#                 head += c
#
#             # NUMBER
#             elif c.isdigit() and not number_flag:
#                 head_flag = True
#                 number += c
#
#                 if len(number) >= 5:
#                     number_flag = True
#
#             # TAIL
#             else:
#                 # TAIL
#                 number_flag = True
#                 tail += c
#
#
#         result.append([head, number, tail])
#
#     return result


if __name__=="__main__":
    #files = ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]
    files = ["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "a01-01", "A-011 Thunderbolt II", "a-10 Thunderbolt II", "A-010 Thunderbolt II", "F-14 Tomcat", "F-150000000", "F-15", "f-15"]

    answer = solution(files)
    print(answer) # ["img1.png", "IMG01.GIF", "img02.png", "img2.JPG", "img10.png", "img12.png"]
                  # ["A-10 Thunderbolt II", "B-50 Superfortress", "F-5 Freedom Fighter", "F-14 Tomcat"]