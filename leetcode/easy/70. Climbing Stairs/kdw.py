class Solution:
    def climbStairs(self, n: int) -> int:
        curr = prev1 = prev2 = 1
        for _ in range(1, n):
            curr = prev1 + prev2
            prev1, prev2 = curr, prev1
        return curr
