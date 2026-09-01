class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        hashmap = {}
        for i in range(len(order)):
            hashmap[order[i]] = i
        # print(hashmap)
        def checkAdj(first, second):
            # print(first, second)
            shortest = min(len(first), len(second))
            for i in range(shortest):
                if hashmap[first[i]] > hashmap[second[i]]:
                    return False
                elif hashmap[first[i]] < hashmap[second[i]]:
                    return True
            if len(first) > len(second):
                return False
            return True
        for i in range(len(words) -1):
            if not checkAdj(words[i], words[i + 1]):
                return False
        return True
            
        