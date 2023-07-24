class Solution:
    # using set
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = left = right = 0
        window = set()
        len_s = len(s)

        while right < len_s:
            if s[right] not in window:
                window.add(s[right])
                right += 1
                max_length = max(max_length, right - left)
            else:
                window.remove(s[left])
                left += 1

        return max_length

    # using dictionary
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = start = 0
        visited = {}

        for i, char in enumerate(s):
            if char in visited:
                start = max(start, visited[char] + 1)
            visited[char] = i
            max_length = max(max_length, i - start + 1)

        return max_length
