class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        answer = None
        cnt = 0
        for num in nums:
            if answer == num:
                cnt += 1
            elif not cnt:
                answer = num
                cnt = 1
            else:
                cnt -= 1
        return answer
