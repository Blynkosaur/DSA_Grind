class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        times = [(position[i],(target- position[i])/speed[i]) for i in range(len(position))]
        #speed = distance/time
        times.sort(reverse = True)
        count = 0
        prev = None
        for time in times:
            if not prev:
                count += 1
                prev = time
            else:
                if time[1] > prev[1]:
                    count+= 1
                    prev = time
        return count
            
            

