class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        maximum = 0
        dfs = deque([])
        for row in range(len(grid)):
            for column in range(len(grid[0])):
                if grid[row][column] == 2:
                    
                    dfs.append([row,column,0])
        count = 0
        while dfs:
            cord = dfs.popleft()
            locrow = cord [0]
            loccol = cord [1]
            time = cord [2]
            node = grid [locrow] [loccol]
            if node == 1:
                count = max(count, time)
                grid [locrow][loccol] = 3


            if locrow < len(grid)-1 :
                if grid [locrow+1][loccol] ==1:
                    dfs.append([locrow+1,loccol,time+1])
            if locrow > 0 :
                if grid [locrow-1][loccol] ==1 :
                    dfs.append([locrow-1,loccol,time+1])
            if loccol < len(grid[row])-1 :
                if grid [locrow][loccol+1] ==1:
                    dfs.append([locrow,loccol+1,time+1])
            if loccol > 0 :
                if grid [locrow][loccol-1] ==1:
                    dfs.append([locrow,loccol-1,time+1])
            maximum = max(maximum,count)
        for row in range(len(grid)):
            for column in range(len(grid[0])):
                if grid[row][column] == 1:
                    return -1
        return maximum 