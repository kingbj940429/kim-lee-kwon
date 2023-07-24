class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = left = right = 0
        window = set()
        len_s = len(s)

        while right < len_s:
            if s[right] not in window:
                window.add(s[right])
                right += 1
                max_length = max(max_length, len(window))
            else:
                window.remove(s[left])
                left += 1

        return max_length
