class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit, buy = 0, prices[0]
        for sell in prices:
            if buy > sell:
                buy = sell
            elif profit < sell - buy:
                profit = sell - buy
        return profit
