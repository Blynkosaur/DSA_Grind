class Solution:
    def reorganizeString(self, s: str) -> str:
        unavailable = deque()
        count = Counter(s)
        heap = []
        answer = ""
        for c in count:
            heapq.heappush(heap, (-1 * count[c], c))
        time = 0
        while heap or unavailable:
            if unavailable and unavailable[0][1] != answer[-1]:
                count, c = unavailable.popleft()
                heapq.heappush(heap, (count,c))
            elif unavailable and not heap:
                break
            count, c = heapq.heappop(heap)
            answer += c
            if count + 1 < 0:
                unavailable.append((count + 1, c))
        return answer if len(answer) == len(s) else ""
            

        



        