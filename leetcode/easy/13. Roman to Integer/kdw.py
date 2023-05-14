class Solution:
    def romanToInt(self, s: str) -> int:
        dic = {'I': 1,
               'V': 5,
               'X': 10,
               'L': 50,
               'C': 100,
               'D': 500,
               'M': 1000}

        answer = prev = 0
        for symbol in s:
            curr = dic[symbol]
            if prev < curr:
                answer += curr - prev - prev
            else:
                answer += curr
            prev = curr
        return answer
