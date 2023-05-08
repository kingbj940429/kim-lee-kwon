from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = 0
        for letters in zip(*strs):
            if len(set(letters)) != 1:
                break
            prefix += 1
        return strs[0][:prefix] if prefix else ''


solution = Solution()
print(solution.longestCommonPrefix(strs=["flower", "flow", "flight"]))  # "fl"
print(solution.longestCommonPrefix(strs=["dog", "racecar", "car"]))  # ""
