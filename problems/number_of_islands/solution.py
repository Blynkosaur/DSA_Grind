class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        islands = 0
        def bfs(r, c):
            q = deque([(r,c)])
            dirs = [(-1,0), (1,0), (0,-1), (0, 1)]
            while q:
                r,c = q.popleft()
                visited.add((r,c))
                for dx, dy in dirs:
                    px, py = r + dx, c + dy
                    if px in range(rows) and py in range(cols) and (px, py) not in visited and grid[px][py] == "1":
                        q.append((px,py))
                        visited.add((px,py))
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1" and (r,c) not in visited:
                    bfs(r,c)
                    islands += 1
        return islands



        