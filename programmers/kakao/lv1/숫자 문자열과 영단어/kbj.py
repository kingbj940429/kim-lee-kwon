def solution(s):
    eng = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    answer = ""
    temp_word = ""

    for val in s:
        if val.isdigit():
            answer += val
        else:
            temp_word += val

            if temp_word in eng:
                answer += str(eng.index(temp_word))
                temp_word = ""


    return int(answer)