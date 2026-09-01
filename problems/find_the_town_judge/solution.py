class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trusting = set()
        trusted = defaultdict(int) 
        for i in range(1, n + 1):
            trusting.add(i)
        for t in trust:
            trusting.discard(t[0])
            trusted[t[1]] += 1
        # print(trusting, trusted)
        if len(trusting) != 1 or trusted[next(iter(trusting))] != n -1:
            return -1
        return next(iter(trusting))
        