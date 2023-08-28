class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)

        def findFirst(target):
            left, right = 0, n - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return left

        first = findFirst(target)
        if first != n and nums[first] == target:
            return [first, findFirst(target + 1) - 1]
        return [-1, -1]
