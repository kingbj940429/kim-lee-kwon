# 문제이해 > 접근방식 > 코드설계 > 코드구현

def solution(s):
    answer = []

    # cut 단위
    for i in range(1, len(s) + 1):
        per_cut = i
        result = ""
        cnt = 1

        for j in range(0, len(s), per_cut):
            current_word = s[j:j+per_cut]
            next_word = s[j + per_cut : j + per_cut + per_cut]

            if current_word == next_word:
                cnt += 1
            else:
                if cnt > 1:
                    result += str(cnt) + current_word
                    cnt = 1
                else:
                    result += current_word

        answer.append(len(result))

    return min(answer)

if __name__=="__main__":
    s = "abcabcabcabcdededededede"

    print(solution(s)) # 14