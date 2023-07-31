class Solution:
    # Dynamic Programming
    # Time complexity: O(n^2)
    # Space complexity: O(n^2)
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[True for _ in range(n)] for _ in range(n)]
        start = end = 0

        for i in range(1, n):
            for j in range(n - i):
                if s[j] == s[i + j] and dp[j + 1][i + j - 1]:
                    start, end = j, i + j
                else:
                    dp[j][i + j] = False

        return s[start:end + 1]

    # Expand From Centers
    # Time complexity: O(n^2)
    # Space complexity: O(1)
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        start = end = 0
        length = 1

        def expand(left, right):
            nonlocal start, end, length

            while left > -1 and right < n and s[left] == s[right]:
                left -= 1
                right += 1

            if right - left - 1 > length:
                start, end, length = left + 1, right - 1, right - left - 1

        for center in range(n):
            expand(center, center)
            expand(center, center + 1)

        return s[start:end + 1]
