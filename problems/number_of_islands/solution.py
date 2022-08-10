class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
            count = 0
            visited= [[False for i in range(len(grid[0]))] for j in range(len(grid))]
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j] == "1" and visited[i][j] == False:
                        q = deque()
                        q.append((i,j))
                        visited[i][j] = True
                        while len(q) != 0:
                            coord = q.popleft()
                            x = coord[0]
                            y = coord[1]
                            if x-1 >= 0 and grid[x-1][y] == "1" and visited[x-1][y] == False:
                                q.append((x-1,y))
                                visited[x-1][y]= True
                            if x+1 < len(grid)  and grid[x+1][y] == "1" and visited[x+1][y] == False:
                                q.append((x+1,y))
                                visited[x+1][y]= True
                            if y-1 >= 0 and grid[x][y-1] == "1" and visited[x][y-1] == False:
                                q.append((x,y-1))
                                visited[x][y-1]= True
                            if y+1 < len(grid[0]) and grid[x][y+1] == "1" and visited[x][y+1] == False:
                                q.append((x,y+1))
                                visited[x][y+1]= True
                        count +=1
            return count