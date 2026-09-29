class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        if sum(matchsticks) % 4 or len(matchsticks) < 4:
            return False
        target = sum(matchsticks)//4
        print(sum(matchsticks),target)
        count = Counter(matchsticks)
        # print(count)
        vals = sorted(count, reverse=True)
        def backtrack(partition,remaining):
            # print(partition,count)
            if remaining ==0:
                return partition[0] == partition[1] == partition[2] == partition[3]
            for match in vals:
                if not count[match]:
                    continue
                count[match] -= 1
                if not partition or partition[-1] == target:
                    partition.append(match)
                    if backtrack(partition, remaining-1):
                        return True
                    count[match] += 1
                    partition.pop()
                    return False
                elif partition[-1] + match <= target:
                    partition[-1] += match
                    if backtrack(partition, remaining - 1):
                        return True
                    partition[-1] -= match
                count[match] += 1
            return False
        if backtrack([], len(matchsticks)):
            return True
        return False
            
            
                

                

        
        