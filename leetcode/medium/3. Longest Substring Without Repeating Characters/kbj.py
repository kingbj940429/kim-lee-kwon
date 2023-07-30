from collections import deque

class Solution:
    def lengthOfLongestSubstring(self, s) -> int:
        q = deque()
        result = 0

        for c in s:
            if c not in q:
                q.append(c)

            else:
                result = max(len(q), result)

                while q:
                    first = q.popleft()

                    # 일치하는 글자가 있을때까지 while 문 돌다가 있으면 break
                    if first == c:
                        q.append(first)
                        break

        return max(result, len(q))


if __name__ == "__main__":
    s = "dvdf"
    solution = Solution()
    result = solution.lengthOfLongestSubstring(s)
    print(result) # 3
