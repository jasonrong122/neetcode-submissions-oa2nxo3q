class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = len(prices) - 1
        l_shift = 0
        r_shift = len(prices) - 1

        while l <= r_shift:
            if prices[l_shift] < prices[l]:
                l = l_shift
                
            if prices[r_shift] > prices[r]:
                r = r_shift
            
            l_shift += 1
            r_shift -= 1
        
        if prices[l] > prices[r]:
            return 0

        return prices[r] - prices[l]
            