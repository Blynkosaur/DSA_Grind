class TrieNode:
    def __init__(self):
        self.eow = False
        self.children = {}
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        node = self.root
        for i in range(len(word)):
            char = word[i] 
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.eow = True
    def search(self, word: str) -> bool:
        stack = [(self.root, 0)]
        while stack:
            node, index = stack.pop()
            if index >= len(word):
                continue
            char = word[index]
            if char == ".":
                for c in node.children:
                    if node.children[c].eow == True and index == len(word) - 1:
                        return True
                    stack.append((node.children[c], index + 1))
                continue
            elif char in node.children:
                if node.children[char].eow == True and index == len(word)-1:
                    return True
                else:
                    stack.append((node.children[char], index + 1))
        return False
            

            
             
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)