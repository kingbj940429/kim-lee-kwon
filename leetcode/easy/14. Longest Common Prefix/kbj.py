# 문제이해 > 접근방식 > 코드설계 > 코드구현

# 가장 길이가 짧은 단어 기준으로 비교할 것
# 한글자 한글자 검색하되, 단어의 전체 갯수와 같지 않으면 바로 결과 리턴

class Solution:
    def longestCommonPrefix(self, words) -> str:
        min_word = words[sorted([[idx,[len(word)]] for idx, word in enumerate(words)], key=lambda x: x[1])[0][0]]
        words_cnt = len(words)
        result = ""

        for i, c in enumerate(min_word):
            common_cnt = 0
            for word in words:
                if word[i] == c:
                    common_cnt += 1
            if common_cnt == words_cnt:
                result += c
            else:
                break

        return result

    def longestCommonPrefixBest(self, words) -> str:
        result = ""

        for i in zip(*words):
            print(i)
            if len(set(i)) == 1:
                result += i[0]
            else:
                return result

        return result



if __name__=="__main__":
    strs = ["flower","flow","flight"]
    solution = Solution()
    print(solution.longestCommonPrefix(strs))
    print(solution.longestCommonPrefixBest(strs))
