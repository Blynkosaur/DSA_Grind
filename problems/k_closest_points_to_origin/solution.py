class Solution:
    def takeSecond(self,elem):
        return elem[1]
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        toreturn = []
        distances = []
        for i in points:
            toadd = (i[0]**2)+(i[1]**2)
            distances.append((i,toadd))
        distances.sort(key=self.takeSecond)
        for i in range(k):
            toreturn.append(distances[i][0])
        return toreturn
            
        
        