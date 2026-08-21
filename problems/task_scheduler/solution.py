class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        timeout = defaultdict(int)
        heap = []
        time = 0
        for t in tasks:
            timeout[t] += 1
        for t in timeout:
            #turn the hashmap into a timeout table
            heapq.heappush(heap, (  -1*timeout[t], t))
            timeout[t] = -1 * n
        queue = deque() # (count, task, time)
        while heap or queue:
            # print(heap, queue)
            time += 1
            if queue:
                if time - queue[0][2] > n:
                    count, task, available = queue.popleft()
                    heapq.heappush(heap, (count, task))
                    # print("added", (count,task))
            if heap:
                count, next_task = heapq.heappop(heap)
                # print(next_task)
                # print(time)
                if count + 1 < 0:
                    queue.append((count + 1, next_task, time))
        return time

            
            
        
        
        