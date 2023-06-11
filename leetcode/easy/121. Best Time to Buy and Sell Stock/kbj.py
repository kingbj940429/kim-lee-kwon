class Solution:
    def maxProfit(self, prices):
        profit = 0
        low = 99999
        for price in prices:
            if low > price:
                low = price
            elif price - low > profit:
                profit = price - low
        return profit


if __name__ == "__main__":
    prices = [7,1,5,3,6,4]
    #prices = [2,4,1]

    solution = Solution()
    result = solution.maxProfit(prices)

    print(result)
