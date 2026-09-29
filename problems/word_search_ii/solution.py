class TrieNode:
    def __init__(self):
        self.children = {}
        self.eow = False
        self.word = ""
class Trie:
    def __init__(self, words):
        self.root = TrieNode()
        for word in words:
            self.insert(word)

    def insert(self, word) -> None:
        node = self.root
        for i in range(len(word)):
            char = word[i]
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.eow = True
        node.word = word
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie(words).root
        found = []
        def dfs(x,y,node, path, parent):
            char = board[x][y]
            # print(char)
            #check for already traversed cells
            if (x,y) in path:
                # print("already in path")
                return 
            #not a prefix so STOP HERE
            if char not in node.children:
                # print("end")
                return
            #move to the next node
            parent = node
            node = node.children[char]
            #check if end of word
            if node.eow:
                node.eow = False
                found.append(node.word)
                if not node.children:
                    parent.children.pop(char)
                # print(node.word)
            path.add((x,y))
            if x < len(board) - 1 : #up 
                dfs(x + 1, y, node, path, parent )
            if x > 0 : #down
                dfs(x - 1, y, node, path, parent)
            if y < len(board[0]) - 1 : #right
                dfs(x, y + 1, node, path, parent)
            if y > 0 : #left
                dfs(x , y - 1, node, path, parent)
            path.remove((x,y))
            
        for i in range(len(board)):
            for j in range(len(board[0])):
                # print(board[i][j], "first")
                dfs(i,j,trie,set(), None)
        return found 

        