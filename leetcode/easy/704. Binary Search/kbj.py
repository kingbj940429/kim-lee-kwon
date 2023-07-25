from bisect import bisect_left, bisect_right

class Solution:

    def search(self, nums, target) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        else:
            return -1

    def search2(self, nums, target) -> int:
        return bisect_left(nums, target) if target in nums else -1

if __name__=="__main__":
    nums = [-1, 0, 3, 5, 9, 12]
    target = 9

    solution = Solution()
    result = solution.search(nums, target)

    print(result) # 4
