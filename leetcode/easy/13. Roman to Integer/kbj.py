# 문제이해 > 접근방식 > 코드설계 > 코드구현

import re
from collections import defaultdict
class Solution:
    def romanToInt(self, s: str) -> int:
        answer = 0
        roman = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        subtraction_roman = defaultdict(int)
        subtraction_roman["IV"] = 4
        subtraction_roman["IX"] = 9
        subtraction_roman["XL"] = 40
        subtraction_roman["XC"] = 90
        subtraction_roman["CD"] = 400
        subtraction_roman["CM"] = 900

        for key, value in subtraction_roman.items():
            answer += re.subn(key, "", s)[1] * value
            s = re.subn(key, "", s)[0]

        for c in s:
            answer += roman[c]

        return answer

    def romanToInt2(self, s: str) -> int:
        skip = False
        answer = 0

        roman = {
            " ": 0,
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        s += " "

        for i, c in enumerate(s):
            if skip or c == " ":
                skip = False
                continue
            else:
                if roman[c] < roman[s[i+1]]:
                    answer += roman[s[i+1]] - roman[c]
                    skip = True
                else:
                    answer += roman[c]
        return answer

if __name__=="__main__":
    solution = Solution()
    s = "MCMXCIV"
    print(solution.romanToInt(s))