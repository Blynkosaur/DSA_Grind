class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        monotonic_stack = []
        output = [0 for _ in range(len(temperatures))]
        for i in range(len(temperatures)):
            while monotonic_stack and monotonic_stack[-1][0] < temperatures[i]:
                last = monotonic_stack.pop()
                output[last[1]] = i - last[1]  
            monotonic_stack.append((temperatures[i], i))
        return output

                



        