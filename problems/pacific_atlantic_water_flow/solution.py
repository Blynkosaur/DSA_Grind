class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific = deque()
        for i in range(len(heights)):
            pacific.append((i,0))
        for i in range(len(heights[0])):
            pacific.append((0,i))
        pvisited = set(pacific)
        while pacific:
            island = pacific.popleft()
            pvisited.add(island)
            height = heights[island[0]] [island[1]]
            if island[0] > 0:
                up = (island[0]-1,island[1])
                if up not in pvisited and heights[up[0]][up[1]] >= height:
                    pacific.append(up)
            if island[0] < len(heights)-1:
                down = (island[0]+1, island[1])
                if down not in pvisited and heights[down[0]][down[1]] >= height:
                    pacific.append(down)
            if island[1] > 0:
                left = (island[0], island[1]-1)
                if left not in pvisited and heights[left[0]][left[1]] >= height:
                    pacific.append(left)
            if island[1] < len(heights[0])-1:
                right = (island[0], island[1] +1)
                if right not in pvisited and heights[right[0]][right[1]] >= height:
                    pacific.append(right)
        atlantic = deque()
        for i in range(len(heights)):
            atlantic.append((i,len(heights[0])-1))
        for i in range(len(heights[0])):
            atlantic.append((len(heights)-1,i))
        avisited = set(atlantic)
        while atlantic:
            island = atlantic.popleft()
            avisited.add(island)
            height = heights[island[0]] [island[1]]
            if island[0] > 0:
                up = (island[0]-1,island[1])
                if up not in avisited and heights[up[0]][up[1]] >= height:
                    atlantic.append(up)
            if island[0] < len(heights)-1:
                down = (island[0]+1, island[1])
                if down not in avisited and heights[down[0]][down[1]] >= height:
                    atlantic.append(down)
            if island[1] > 0:
                left = (island[0], island[1]-1)
                if left not in avisited and heights[left[0]][left[1]] >= height:
                    atlantic.append(left)
            if island[1] < len(heights[0])-1:
                right = (island[0], island[1] +1)
                if right not in avisited and heights[right[0]][right[1]] >= height:
                    atlantic.append(right)
            
        return list(pvisited.intersection(avisited))