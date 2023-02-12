def convert(n, k):
    mods = []
    while n:
        n, mod = divmod(n, k)
        mods.append(str(mod))
    return ''.join(reversed(mods))


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if not num % i:
            return False
    return True


def solution(n, k):
    answer = 0
    n = convert(n, k)
    for i in n.split('0'):
        if i and is_prime(int(i)):
            answer += 1
    return answer
