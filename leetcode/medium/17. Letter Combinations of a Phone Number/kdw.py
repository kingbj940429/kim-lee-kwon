class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        answer = []
        mapping = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        n = len(digits)

        def combine(i, letters):
            if i == n:
                answer.append(letters)
                return
            for letter in mapping[digits[i]]:
                combine(i + 1, letters + letter)

        combine(0, '')
        return answer
