class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if beginWord not in wordList:
            wordList.append(beginWord)
        
        graph = {}
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] +"*"+word[i+1:]
                
                if pattern not in graph:
                    graph[pattern] = [word]
                else:

                    graph[pattern].append(word)
        
        queue = deque([beginWord])
        minlen = 1
        visited = set()
        
        print(graph)             
        
        while queue:
            print(queue)
            for i in range(len(queue)):
                word = queue.popleft()
                ls = [word[:i] +"*"+word[i+1:] for i in range(len(word))]
                visited.add(word)
                for patern in ls: 
                    for el in graph[patern]:
                        if el not in visited:
                            if el == endWord:
                                return minlen +1
                            visited.add(el)
                            queue.append(el)

            minlen += 1

        return 0
        
