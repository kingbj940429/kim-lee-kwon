from collections import Counter
class Solution:
    def singleNumber(self, nums):
        counter = Counter(nums)

        for key, value in counter.items():
            if value == 1:
                return key

if __name__ == "__main__":
    nums = [2, 2, 1]
    solution = Solution()
    print(solution.singleNumber(nums))
