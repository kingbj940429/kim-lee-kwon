class Solution:

    def maxArea(self, height) -> int:
        left, right = 0, len(height) - 1
        result = 0

        while left < right:
            w = right - left
            h = min(height[left], height[right])

            area = w * h
            result = max(area, result)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return result

    # 부루트 포스 시간 초과
    def maxArea2(self, height) -> int:
        result = 0
        for i, v in enumerate(height):
            for j in range(i + 1, len(height)):
                if v >= height[j]:
                    h = min(v, height[j])
                    w = j - i

                    area = h*w
                    result = max(result, area)

        return result


if __name__ == "__main__":
    height = [1,8,6,2,5,4,8,3,7]

    solution = Solution()
    result = solution.maxArea(height)
    print(result)

