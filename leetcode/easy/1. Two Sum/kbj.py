# 문제이해 > 접근방식 > 코드설계 > 코드구현

# Dictionary
from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = defaultdict(int)

        for i, num in enumerate(nums):
            diff = target - num

            if diff in dic:
                return [dic[diff], i]

            dic[num] = i


# Two Pointer
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left, right = 0, len(nums) - 1
        for i, v in enumerate(nums):
            nums[i] = [i, v]

        nums.sort(key=lambda x: x[1])

        while left <= right:
            sum_num = nums[left][1] + nums[right][1]
            if sum_num > target:
                right -= 1
            elif sum_num < target:
                left += 1
            else:
                return [nums[left][0], nums[right][0]]
