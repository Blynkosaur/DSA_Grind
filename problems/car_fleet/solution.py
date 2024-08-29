class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        times= []
        two = list(zip(position,speed))
        two = sorted(two)

        for pos in range(len(position)):
            time = (target -two[pos][0])/two[pos][1]
            times.append(time)
        head = times[-1]
        fleets = 0
        for i in range(len(times) - 1, -1, -1):
            if times[i] > head:
                head = times[i]
                fleets += 1
        fleets += 1
        return fleets



            