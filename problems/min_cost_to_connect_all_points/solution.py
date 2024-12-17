class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        adj = {i: [] for i in range(N)}
        for i in range(N):
            x1, y1 = points[i]
            for j in range(i + 1, N):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                adj[i].append([dist, j])
                adj[j].append([dist, i])
        visited = set()
        cost = 0
        # print(adj)
        frontier = [(0,0)]
        while len(visited)!= N:
            # print(frontier)
            time, node = heappop(frontier)
            # print(time,node)
            if node not in visited:
                cost += time
            visited.add(node)
            for nexttime, nextnode in adj[node]:
                if nextnode not in visited:
                    heappush(frontier,(nexttime,nextnode))
                
        return cost

            
            
