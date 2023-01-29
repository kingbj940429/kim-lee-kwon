def solution(n, arr1, arr2):
    return [format(x1 | x2, 'b')
                .zfill(n)
                .replace('1', '#')
                .replace('0', ' ')
            for x1, x2 in zip(arr1, arr2)]
