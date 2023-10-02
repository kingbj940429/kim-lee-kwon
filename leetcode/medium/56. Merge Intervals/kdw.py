class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        answer = [intervals[0]]
        for interval in intervals:
            if answer[-1][1] < interval[0]:
                answer.append(interval)
            elif answer[-1][1] < interval[1]:
                answer[-1][1] = interval[1]
        return answer
