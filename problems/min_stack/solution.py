class MinStack:

    def __init__(self):
        self.stack = []
        

    def push(self, value: int) -> None:
        smallest =  min(value, self.stack[-1][1]) if self.stack else value
        self.stack.append((value,smallest))
        

    def pop(self) -> None:
        return self.stack.pop()[0]
        

    def top(self) -> int:
        return self.stack[-1][0]
        

    def getMin(self) -> int:
        return self.stack[-1][1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()