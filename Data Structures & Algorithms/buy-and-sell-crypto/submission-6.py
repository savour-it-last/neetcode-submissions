class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        buy_i = 0
        sell_i = 1
        while sell_i<len(prices):
            if prices[sell_i] < prices[buy_i]:
                # sell_i+=1
                # buy_i+=1
                buy_i = sell_i
                continue
            current_profit = prices[sell_i] - prices[buy_i]
            if current_profit <= max_profit:
                sell_i+=1
            else:
                max_profit = current_profit
        return max_profit
            
        