class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        max_area = 0
        visited = set()
        def bfs(r,c):
            q = deque([(r,c)])
            dirs = [(-1,0), (1,0), (0,-1), (0, 1)]
            area = 0
            nonlocal max_area
            while q:
                r,c = q.popleft()
                visited.add((r,c))
                area += 1
                for dr, dc in dirs:
                    if r + dr in range(rows) and c + dc in range(cols) and (r+dr, c + dc) not in visited and grid[r+dr][c + dc] == 1:
                        visited.add((r+dr, c + dc))
                        q.append((r+dr, c + dc))
            max_area = max(max_area, area) 

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r,c) not in visited:
                    bfs(r,c)
        return max_area

        
        