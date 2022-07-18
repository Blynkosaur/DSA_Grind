class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maximum = -1*float("inf")
        for i in accounts:
            local = sum(i)
            maximum = max(local,maximum)
        return maximum