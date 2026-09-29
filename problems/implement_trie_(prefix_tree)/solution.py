class TrieNode:
    def __init__(self):
        self.children = {}
        self.eow = False
class Trie:

    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        node = self.root
        for i in range(len(word)):
            if word[i] not in node.children:
                node.children[word[i]] = TrieNode()
            node = node.children[word[i]]
            if i == len(word)-1:
                node.eow = True

    def search(self, word: str) -> bool:
        node = self.root
        for i in range(len(word)):
            if word[i] not in node.children:
                return False
            node = node.children[word[i]]
            if i == len(word)-1 and node.eow == False:
                return False
        return True

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for i in range(len(prefix)):
            if prefix[i] not in node.children:
                return False
            node = node.children[prefix[i]]
        return True

    
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)