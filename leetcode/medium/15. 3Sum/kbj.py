class Solution:

    # two pointer
    def threeSum(self, nums):
        result = []
        nums.sort()

        for i, num in enumerate(nums):
            current = num
            left, right = i + 1, len(nums) - 1

            while left < right:
                total = current + nums[left] + nums[right]

                if total == 0:
                    if sorted([current, nums[left], nums[right]]) not in result:
                        result.append([current, nums[left], nums[right]])
                    left += 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1

        return result


if __name__ == "__main__":
    nums = [-1, 0, 1, 2, -1, -4, -1, 0, 1]
    # [-4, -1, -1, 0, 1, 2]

    solution = Solution()
    print(solution.threeSum(nums)) # [[-1,-1,2],[-1,0,1]]
