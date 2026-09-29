class Solution:
    def possible(self,weight: List[int], cap:int)-> int:
        days = 0
        curr_load = 0 
        for w in weight:
            if curr_load + w <= cap:
                curr_load += w
            else:
                curr_load = w
                days += 1
        return days + 1

    def shipWithinDays(self, weights: List[int], days: int) -> int:
        min_cap = max(weights)
        max_cap = min_cap * len(weights)
        glob = max_cap
        while min_cap <= max_cap:
            mid = min_cap + (max_cap - min_cap)//2
            ret_possible = self.possible(weights,mid)
            if ret_possible == days or ret_possible < days:
                glob = min(glob, mid)
                max_cap = mid - 1
            else:
                min_cap = mid + 1
        if self.possible(weights,mid) == days:
            glob = min(glob,mid)
        return glob

            
        