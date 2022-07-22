class MyQueue:

    def __init__(self):
        self.st = []
        self.s2 = []
        

    def push(self, x: int) -> None:
        
        self.st.append(x)

    def pop(self) -> int:
        for i in range(len(self.st)-1):
                self.s2.append(self.st.pop())
        toreturn =self.st.pop()
        for i in range(len(self.s2)):
            self.st.append(self.s2.pop())
        print(self.st)
        return toreturn
    def peek(self) -> int:
        for i in range(len(self.st)-1):
                self.s2.append(self.st.pop())
        toreturn = self.st.pop()
        self.push(toreturn)
        for i in range(len(self.s2)):
            self.st.append(self.s2.pop())
        return toreturn
    

    def empty(self) -> bool:
        if len(self.st) ==0 :
            return True
        return False
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()