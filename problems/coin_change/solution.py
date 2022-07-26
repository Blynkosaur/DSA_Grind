class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # total = 0
        # number = 0
        # while coins:
        #     if total + max(coins) <= amount:
        #         total += max(coins)
        #         number += 1
        #     else:
        #         coins.remove(max(coins))
        # if total < amount:
        #     return -1
        # return number
        dp = [0] + [float('inf')] * amount
        
        for coin in coins:
            for i in range(coin, amount+1):
                dp[i] = min(dp[i], dp[i-coin]+1)
        
        return dp[-1] if dp[-1] != float('inf') else -1
            
        