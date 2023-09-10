class Solution:
    def combinationSum(self, candidates, target):
        result = []
        total = len(candidates)

        def dfs(cur_list, cur_sum, idx):
            if cur_sum > target:
                return
            elif cur_sum == target:
                result.append(cur_list)

            for i in range(idx, total):
                dfs(cur_list + [candidates[i]], cur_sum + candidates[i], i)

        dfs([], 0, 0)

        return result


if __name__=="__main__":
    candidates = [2, 3, 6, 7]
    target = 7

    solution = Solution()
    result = solution.combinationSum(candidates, target)
    print(result)
