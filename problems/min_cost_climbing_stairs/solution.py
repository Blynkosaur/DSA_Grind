class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        dp = {0:cost[0],1:cost[1]}
        for i in range(2,len(cost)):
            mincost = cost[i]+min(dp[i-1],dp[i-2])
            dp[i] = mincost
        print(dp)
        return min(dp[len(cost)-1],dp[len(cost)-2])