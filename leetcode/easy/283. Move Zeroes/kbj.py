class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        zero_pos = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[zero_pos] = nums[zero_pos], nums[i]
                zero_pos += 1
