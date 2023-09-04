class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        answer = []
        candidates.sort()
        n = len(candidates)

        def backtracking(chosen, target, start):
            for i in range(start, n):
                candidate = candidates[i]
                if candidate > target:
                    return
                if candidate == target:
                    answer.append(chosen + [candidate])
                    return
                backtracking(chosen + [candidate], target - candidate, i)

        backtracking([], target, 0)
        return answer
