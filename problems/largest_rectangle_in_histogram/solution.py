class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maximum = 0
        stack = []
        areas = []
        for i,h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                start = index
                area = height * (i-index)
                areas.append(area)
                
            stack.append((start,h))
        
        for el in stack:
            i,h = el[0],el[1]
            area = h *(len(heights)-i)
            areas.append(area)
        
        return max(areas)
        