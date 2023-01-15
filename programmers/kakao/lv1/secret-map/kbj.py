def solution(n, arr1, arr2):
    return sum_arr(n, arr1, arr2)

def sum_arr(n, arr1, arr2):
    answers = []

    for i in range(n):
        sums = str(int(format(arr1[i], 'b')) + int(format(arr2[i], 'b')))
        filled_sum = fill_zero(n, sums)
        answers.append(filled_sum.replace('2', '#').replace('1', '#').replace('0', ' '))

    return answers

def fill_zero(n, value):
    format_str = '0' + str(n)
    return format(int(value), format_str)