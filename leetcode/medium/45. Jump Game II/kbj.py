from collections import deque


class Solution:

    # Referred to Solution
    def jump(self, nums) -> int:
        reach, count, last = 0, 0, 0

        for i in range(len(nums) - 1):
            reach = max(reach, i + nums[i])

            if i == last:
                last = reach
                count += 1

        return count

    # BFS Memory Limit Exceeded
    # 82 / 109 testcases passed
    def jump2(self, nums) -> int:
        goal = len(nums) - 1
        q = deque()
        q.append([nums[0], 0, 0])  # number, idx

        while q:
            cur_val, cur_idx, depth = q.popleft()

            if cur_idx == goal:
                return depth

            for i in range(1, cur_val + 1):
                if cur_idx + i <= goal:
                    q.append([nums[cur_idx + i], cur_idx + i, depth + 1])

if __name__ == "__main__":
    # nums = [2, 3, 1, 1, 4]
    nums = [2, 3, 0, 1, 4]
    solution = Solution()
    result = solution.jump(nums)

    print(result)
