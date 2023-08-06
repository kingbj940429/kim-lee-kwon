class Solution:

    # Manacher's Algorithm
    def longestPalindrome(self, s) -> str:

        def expand(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l+1:r]

        result = ""
        for i in range(len(s)):
            sub1 = expand(i, i)
            if len(sub1) > len(result):
                result = sub1

            sub2 = expand(i, i+1)
            if len(sub2) > len(result):
                result = sub2

        return result

if __name__ == "__main__":
    s = "babbabd"
    solution = Solution()
    result = solution.longestPalindrome(s)

    print(result)
