class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for sp_i in range(1,len(prices)):
            min_cp = min(prices[:sp_i])
            curr_profit = prices[sp_i] - min_cp
            if curr_profit<=0 or curr_profit<=max_profit:
                continue
            max_profit = curr_profit

        return max_profit

        