class StockSpanner:

    def __init__(self):
        self.stack = [(float("inf"),-1)]
        self.days = 0

    def next(self, price: int) -> int:
        if not self.stack:
            self.stack.append((price,self.days))
            self.days += 1
            return 1
        else:
            popped = False
            while self.stack and self.stack[-1][0] <= price:
                popped = True 
                self.stack.pop()
            span = self.days- self.stack[-1][1] if popped else 1
            self.stack.append((price,self.days))
        self.days += 1
        return span 

            
        
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)