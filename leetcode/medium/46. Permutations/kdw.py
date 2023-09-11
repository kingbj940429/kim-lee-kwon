class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        answer = []
        n = len(nums)
        visited = [False for _ in range(n)]
        path = []

        def dfs(depth):
            if depth == n:
                answer.append(path[:])
                return
            for i in range(n):
                if not visited[i]:
                    visited[i] = True
                    path.append(nums[i])
                    dfs(depth + 1)
                    path.pop()
                    visited[i] = False

        dfs(0)
        return answer
