class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0

        l = 0
        max_profit = 0

        for r in range(1, len(prices) - 1):
            max_profit = max(max_profit, prices[r] - prices[l])

            if prices[r] < prices[l]:
                l = r
        
        return max_profit
