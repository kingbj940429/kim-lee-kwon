class Solution:
    # Dynamic Programming
    # Time complexity: O(m * n)
    # Space complexity: O(m * n)
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1 for _ in range(n)] for _ in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[-1][-1]

    # Dynamic Programming - Space Optimization
    # Time complexity: O(m * n)
    # Space complexity: O(min(m, n)), but this code is O(n).
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [1 for _ in range(n)]
        for _ in range(1, m):
            for i in range(1, n):
                dp[i] += dp[i - 1]
        return dp[-1]

    # Math, Combinatorics
    # Time complexity: O(min(m, n))
    # Space complexity: O(1)
    def uniquePaths(self, m: int, n: int) -> int:
        return comb(m + n - 2, m - 1)
