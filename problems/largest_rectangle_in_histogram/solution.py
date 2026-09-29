class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = heights[0]
        monotonic = [(heights[0],0)]
        for i, height in enumerate(heights):
            # print(f"monotonic {monotonic}")
            if i == 0:
                continue
            if height >= monotonic[-1][0]:
                monotonic.append((height,i))
            else:
                last_index = 0
                while monotonic and height < monotonic[-1][0]:
                    new_height, last_index = monotonic.pop()
                    new_area = new_height * (i-last_index)
                    max_area = max(max_area, new_area)
                monotonic.append((height,last_index))
        while monotonic:
            height, index = monotonic.pop()
            new_area = height * (len(heights)-index)
            max_area = max(max_area, new_area)
            
        return max_area

         


        