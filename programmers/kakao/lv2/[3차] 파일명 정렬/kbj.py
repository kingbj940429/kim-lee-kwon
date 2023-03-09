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

# def solution(files):
#     a = sorted(files, key=lambda file : int(re.findall('\d+', file)[0]))
#     b = sorted(a, key=lambda file : re.split('\d+', file.lower())[0])
#     return b

def solution(files):
    return sorted(files, key=lambda file: (find_head_and_number(file)))

def find_head_and_number(file):
    head, number, tail = re.match("([a-zA-Z-. ]+)(\d{1,5})(.*)", file).groups()

    return [head.lower(), int(number)]

if __name__=="__main__":
    #files = ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]
    files = ["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "a01-01", "A-011 Thunderbolt II", "a-10 Thunderbolt II", "A-010 Thunderbolt II", "F-14 Tomcat", "F-150000000", "F-15", "f-15"]

    answer = solution(files)
    print(answer) # ["img1.png", "IMG01.GIF", "img02.png", "img2.JPG", "img10.png", "img12.png"]
                  # ["A-10 Thunderbolt II", "B-50 Superfortress", "F-5 Freedom Fighter", "F-14 Tomcat"]