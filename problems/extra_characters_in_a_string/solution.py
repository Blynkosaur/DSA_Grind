class TrieNode:
    def __init__(self):
        self.children = {}
        self.eow = False 
class Trie:
    def __init__(self, words):
        self.root = TrieNode()
        for word in words:
            self.insert(word) 

    def insert(self, word):
        node = self.root
        for i in range(len(word)):
            char = word[i]
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.eow = True
class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        hashmap = {len(s):0}
        trie = Trie(dictionary).root
        def dfs(index):
            node = trie
            if index in hashmap:
                return hashmap[index]
            #if you skip the current letter
            result = 1 + dfs(index+1)
            for j in range(index, len(s)):
                if s[j] not in node.children:
                    break
                node = node.children[s[j]]
                if node.eow:
                    result = min(result, dfs(j + 1))
                    hashmap[index] = result
            return result
        return dfs(0)
        