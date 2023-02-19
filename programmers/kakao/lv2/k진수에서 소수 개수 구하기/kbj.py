# 문제이해, 접근방식, 코드설계, 코드구현

# 조건

def solution(n, k):
    answer = 0

    converted_nums = [c for c in convert(n, k).split("0") if c.isdigit() and int(c) > 1]

    for num in converted_nums:
        if is_prime(num):
            answer += 1

    return answer

def is_prime(num):
    num = int(num)

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def convert(n, q):
    result = ""

    while n > 0:
        n, mod = divmod(n, q)
        result += str(mod)

    return result[::-1]


if __name__=="__main__":
    n = 110011
    k = 10

    # 3
    print(solution(n, k))