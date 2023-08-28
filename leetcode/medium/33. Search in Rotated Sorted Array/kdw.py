class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left, right = 0, n - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > nums[-1]:
                left = mid + 1
            else:
                right = mid - 1

        left, right = left - n, left - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return (mid + n) % n
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1
