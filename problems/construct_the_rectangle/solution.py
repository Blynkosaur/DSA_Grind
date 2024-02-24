class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        minimum = 1000000000000000
        target = []
        for i in range(1,area+1):
            if area % i!= 0:
                pass
            else:
                complement = area/i
                if complement- i < 0:
                    hehe = i- complement
                else:
                    hehe = complement -i
                if hehe < minimum:
                    minimum = hehe
                    target = [int(complement),i]
        return(target)
