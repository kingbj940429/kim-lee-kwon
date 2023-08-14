class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def combine(parentheses, open, close):
            if open == close == n:
                answer.append(parentheses)
                return

            if open < n:
                combine(parentheses + '(', open + 1, close)

            if close < open:
                combine(parentheses + ')', open, close + 1)

        answer = []
        combine('', 0, 0)
        return answer
