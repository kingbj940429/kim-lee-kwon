from itertools import product

class Solution:
    def climbStairs(self, n) -> int:
        result = 0
        A = [1,2]

        for i in range(n+1):
            for comb in list(product(A, repeat = i)):
                if sum(comb) == n:
                    print(comb)
                    result += 1

        return result


if __name__=="__main__":
    n = 5
    solution = Solution()
    result = solution.climbStairs(n)

    print(result)


#### ???? 뭐지 이문제
