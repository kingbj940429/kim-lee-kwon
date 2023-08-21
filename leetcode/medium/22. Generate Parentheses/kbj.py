from itertools import permutations
from collections import deque

class Solution:

    def generateParenthesis(self, n: int) :
        result = []

        def dfs(left, right, s):
            if len(s) == n*2:
                result.append(s)
                return

            if left < n:
                dfs(left + 1, right, s + "(")

            if right < left:
                dfs(left, right + 1, s + ")")

        dfs(0,0,"")

        return result

    # Brute Force -> Memory Limit Exceeded
    def generateParenthesis2(self, n: int):
        init = ["(", ")"] * n
        result = []

        for arr in list(permutations(init, r=n*2)):
            is_valid = self.checkParnethesis(arr)

            if is_valid:
                result.append("".join(arr))

        return list(set(result))

    def checkParnethesis(self, parnethesis):
        stack = deque()

        for p in parnethesis:
            if not stack and p == ")":
                return False

            elif p == "(":
                stack.append(p)

            else:
                stack.pop()
        else:
            return True

if __name__ == "__main__":
    n = 3

    solution = Solution()
    result = solution.generateParenthesis(n) # ["((()))","(()())","(())()","()(())","()()()"]

    print(result)
