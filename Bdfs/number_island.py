def numIslands(self, grid: List[List[str]]) -> int:
        seen = set()
        island_count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i,j) in seen:
                    continue
                else:
                    if grid[i][j] == "1":
                        bfs = deque()
                        bfs.append((i,j))
                        island_count += 1
                        while(bfs):
                            popped = bfs.pop()
                            seen.add(popped)
                            x = popped[0]
                            y = popped[1]
                            if x> 0 and (x-1, y) not in seen and grid[x-1][y] == "1":
                                bfs.append((x-1,y))
                            if x < len(grid)-1 and (x+1, y) not in seen and grid[x+1][y] == "1":
                                bfs.append((x+1,y))
                            if y> 0 and (x, y-1) not in seen and grid[x][y-1] == "1":
                                bfs.append((x,y-1))
                            if y < len(grid[0])-1 and (x, y+1) not in seen and grid[x][y+1] == "1":
                                bfs.append((x,y+1))
        return island_count
