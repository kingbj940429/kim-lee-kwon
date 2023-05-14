# 문제이해 > 접근방식 > 코드설계 > 코드구현

# 전형적인 스택 문제

from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()

        for ch in s:
            if ch == "[":
                stack.append("]")
            elif ch == "{":
                stack.append("}")
            elif ch == "(":
                stack.append(")")
            elif not stack or stack.pop() != ch:
                return False
        return not stack