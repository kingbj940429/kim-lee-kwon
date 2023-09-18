class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        answer = -10000
        current = 0

        for num in nums:
            current = max(num, current + num)
            answer = max(answer, current)

        return answer
