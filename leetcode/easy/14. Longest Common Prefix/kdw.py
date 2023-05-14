class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = 0
        for letters in zip(*strs):
            if len(set(letters)) != 1:
                break
            prefix += 1
        return strs[0][:prefix] if prefix else ''
