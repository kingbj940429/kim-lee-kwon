from collections import Counter

class Solution:
    def majorityElement(self, nums):
        majority = len(nums)/2

        counter = Counter(nums)

        for key, value in counter.items():
            if value > majority:
                return key


if __name__ == "__main__":
    nums = [3, 2, 3]
    solution = Solution()
    print(solution.majorityElement(nums))
