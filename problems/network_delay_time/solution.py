class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        nodes = [float('inf') for x in range(n)]
        graph = defaultdict(list)
        for time in times:
            graph[time[0]].append((time[1],time[2]))
        minheap = [(0,k)]
        t = 0
        visited = set()
        # print(graph)
        while minheap:
            time, node = heappop(minheap)
            if node in visited:
                continue 
            visited.add(node)
            t = max(t,time)   
            
            # print(time,node)
            for edge in graph[node]:
                heappush(minheap,(edge[1]+time,edge[0]))
                # print(minheap)
            
            
        if len(visited) != n:
            return -1   
        return t
        

