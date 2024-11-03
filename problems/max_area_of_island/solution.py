class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        maximum = 0

        for row in range(len(grid)):
            for column in range(len(grid[row])):
                if grid[row][column] == 1:
                    count = 0
                    dfs = deque([[row,column]])
                    while dfs:
                        cord = dfs.pop()
                        locrow = cord [0]
                        loccol = cord [1]
                        node = grid [locrow] [loccol]
                        if node == 1:
                            count += 1
                            grid [locrow][loccol] = 0


                        if locrow < len(grid)-1 :
                            if grid [locrow+1][loccol] ==1:
                                dfs.append([locrow+1,loccol])
                        if locrow > 0 :
                            if grid [locrow-1][loccol] ==1 :
                                dfs.append([locrow-1,loccol])
                        if loccol < len(grid[row])-1 :
                            if grid [locrow][loccol+1] ==1:
                                dfs.append([locrow,loccol+1])
                        if loccol > 0 :
                            if grid [locrow][loccol-1] ==1:
                                dfs.append([locrow,loccol-1])
                        
                    maximum = max(maximum,count)
        return maximum