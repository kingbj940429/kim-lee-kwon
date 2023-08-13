from itertools import combinations

class Solution:
    def letterCombinations(self, digits):
        if not digits:
            return []

        result = [""]
        dial = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        for digit in digits:
            temp = []

            for r in result:
                for d in dial[digit]:
                    temp.append(r + d)

            result = temp

        return result

if __name__ == "__main__":
    digits = "23"

    solution = Solution()
    print(solution.letterCombinations(digits)) # ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]


