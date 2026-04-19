class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for cp_i in range(len(prices)-1):
            for sp_i in range(cp_i+1, len(prices)):
                if prices[sp_i]<=prices[cp_i]:
                    continue
                possible_profit = prices[sp_i]-prices[cp_i]
                if possible_profit > max_profit:
                    max_profit = possible_profit
        return max_profit
        