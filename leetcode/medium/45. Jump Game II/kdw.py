class Solution:
    def jump(self, nums: List[int]) -> int:
        answer = maximum = last = 0

        for i in range(len(nums) - 1):
            maximum = max(maximum, i + nums[i])
            if i == last:
                answer += 1
                last = maximum

        return answer
