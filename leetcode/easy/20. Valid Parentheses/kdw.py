class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for bracket in s:
            if bracket == ')':
                if not stack or stack.pop() != '(':
                    return False
            elif bracket == '}':
                if not stack or stack.pop() != '{':
                    return False
            elif bracket == ']':
                if not stack or stack.pop() != '[':
                    return False
            else:
                stack.append(bracket)
        return not stack


solution = Solution()
print(solution.isValid(s="()"))  # true
print(solution.isValid(s="()[]{}"))  # true
print(solution.isValid(s="(]"))  # false
