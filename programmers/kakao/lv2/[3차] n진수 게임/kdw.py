def convert(i, n, dic):
    mods = []
    while i:
        i, mod = divmod(i, n)
        mod = str(mod) if mod < 10 else dic[mod]
        mods.append(mod)
    return reversed(mods)


def solution(n, t, m, p):
    k = ord('A') - 10
    dic = {i: chr(i + k) for i in range(10, 16)}

    all = ['0']
    tm = t * m
    i = 1
    while len(all) < tm:
        all += convert(i, n, dic)
        i += 1

    return ''.join(all[p - 1::m][:t])
