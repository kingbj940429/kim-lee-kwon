# 문제이해 > 접근방식 > 코드설계 > 코드구현

def compress(text, tok_len):
    words = [text[i:i+tok_len] for i in range(0, len(text), tok_len)]
    res = []
    cur_word = words[0]
    cur_cnt = 1
    for a, b in zip(words, words[1:] + ['']):
        if a == b:
            cur_cnt += 1
        else:
            res.append([cur_word, cur_cnt])
            cur_word = b
            cur_cnt = 1
    return sum(len(word) + (len(str(cnt)) if cnt > 1 else 0) for word, cnt in res)

def solution(text):
    return min(compress(text, tok_len) for tok_len in list(range(1, int(len(text)/2) + 1)) + [len(text)])

# def solution(s):
#     answer = []
#
#     # cut 단위
#     for i in range(1, len(s) + 1):
#         per_cut = i
#         result = ""
#         cnt = 1
#
#         for j in range(0, len(s), per_cut):
#             current_word = s[j:j+per_cut]
#             next_word = s[j + per_cut : j + per_cut + per_cut]
#
#             if current_word == next_word:
#                 cnt += 1
#             else:
#                 if cnt > 1:
#                     result += str(cnt) + current_word
#                     cnt = 1
#                 else:
#                     result += current_word
#
#         answer.append(len(result))
#
#     return min(answer)

if __name__=="__main__":
    s = "abcabcabcabcdededededede"

    print(solution(s)) # 14