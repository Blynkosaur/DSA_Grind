class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        directions = [(-1,0), (1,0), (0,1), (0,-1)]
        p = 0 
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if not grid[r][c]:
                    continue
                perim = 4   
                for d in directions:
                    dx, dy = d
                    px, py = r + dx, c + dy
                    if 0 <= px < len(grid) and 0 <= py < len(grid[0]):
                        if grid[px][py]:
                            perim -= 1
                p += perim
        return p
                    

                




        