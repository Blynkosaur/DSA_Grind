class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        order = []
        answer = []
        queue = []
        for i in range(len(tasks)):
            t = tasks[i]
            heapq.heappush(order, (t[0], t[1], i))
        start,duration, index = heapq.heappop(order)
        answer.append(index)
        time = start + duration
        while order or queue:
            # print("order", order)
            if not queue and order and order[0][0] > time:
                time = order[0][0]
                continue
            while order and order[0][0] <= time:
                did_pop = True
                start, duration, index = heapq.heappop(order)
                heapq.heappush(queue, (duration,  index))
            if queue:
                duration, index = heapq.heappop(queue)
                answer.append(index)
                time += duration
        return answer

                
                
