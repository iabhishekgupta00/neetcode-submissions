class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_profit = float('inf')
        max_profit = 0

        for price in prices:
            if price < min_profit:
                min_profit = price

            profit = price - min_profit

            if profit > max_profit:
                max_profit = profit

        return max_profit        