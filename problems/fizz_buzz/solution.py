class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        my = []
        for i in range(1,n+1):
            if i%15 == 0:
                my.append("FizzBuzz")
            elif i%3 == 0:
                my.append("Fizz")
            elif i%5 == 0:
                my.append("Buzz")
            else:
                my.append(str(i))
        return my
            