class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        answer = ""
        heap = [(a * -1, "a"), (b * -1, "b"), (c * -1, "c")]
        heap = [t for t in heap if t[0] != 0]
        heapq.heapify(heap)
        last_consecutive = () 
        while heap:
            count, char = heapq.heappop(heap)
            answer += char
            if count <= -2 and (not last_consecutive or count < last_consecutive[0]):
                answer += char
                if last_consecutive:
                    heapq.heappush(heap, last_consecutive)
                    last_consecutive = ()
                if count + 2 < 0:
                    last_consecutive = (count + 2, char)
                continue
            else:
                if count + 1 < 0:
                    heapq.heappush(heap, (count + 1, char))
                if last_consecutive:
                    heapq.heappush(heap, last_consecutive)
                    last_consecutive = ()
        return answer




        