def solution(files):
    num = {str(i) for i in range(10)}

    dic = {}

    for file in files:
        n = len(file)

        i = 0
        while i < n:
            if file[i] in num:
                break
            i += 1
        head = file[:i]

        j = i
        while j < n:
            if file[j] not in num:
                break
            j += 1
        number = file[i:j]

        dic[file] = head.lower(), int(number)

    return sorted(dic, key=lambda x: dic[x])
