class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        sell = 0
        maximum = 0
        for price in range(len(prices)):
            if prices[price]< prices[buy] and price > buy:
                buy = price
                if buy > sell:
                    sell = buy
            if prices[price]>prices[sell]:
                sell = price
            profits = prices[sell]-prices[buy]
            if profits>maximum:
                maximum = profits
        
            
        return(maximum)
