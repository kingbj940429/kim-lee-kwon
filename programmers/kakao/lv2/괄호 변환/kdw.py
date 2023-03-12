def split(w):
    s = 0
    for i in range(len(w)):
        if w[i] == '(':
            s += 1
        else:
            s -= 1
        if not s:
            break
    return w[:i + 1], w[i + 1:]


def is_correct(u):
    s = 0
    for i in range(len(u)):
        if u[i] == '(':
            s += 1
        else:
            s -= 1
            if s < 0:
                return False
    return True


def reverse(u):
    return ''.join(map(lambda x: ')' if x == '(' else '(', u[1:-1]))


def solution(w):
    if not w:
        return w
    u, v = split(w)
    if is_correct(u):
        return u + solution(v)
    else:
        return '(' + solution(v) + ')' + reverse(u)
