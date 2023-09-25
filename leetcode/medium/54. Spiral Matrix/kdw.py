class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        answer = []
        m, n = len(matrix), len(matrix[0])
        mn = m * n

        for k in range((min(m, n) + 1) // 2):
            for j in range(k, n - k):
                answer.append(matrix[k][j])

            for i in range(k + 1, m - k):
                answer.append(matrix[i][n - k - 1])

            if len(answer) == mn:
                break

            for j in range(n - k - 2, k - 1, -1):
                answer.append(matrix[m - k - 1][j])

            for i in range(m - k - 2, k, -1):
                answer.append(matrix[i][k])

        return answer
