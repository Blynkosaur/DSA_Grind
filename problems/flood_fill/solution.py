class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        r=len(image)
        c=len(image[0])
        
        visited = [[False for i in range(len(image[0]))] for j in range(len(image))]
        
        q= deque()
        q.append((sr,sc))
        # image[sr][sc]=color
        startingColor=image[sr][sc]
        while(q):
            coord= q.popleft()
            x= coord[0]
            y=coord[1]
            

            
            if x-1>=0 and image[x-1][y]==image[x][y] and not visited[x-1][y] :
                # image[x-1][y] = color
                q.append((x-1,y))
            if x+1<r and image[x+1][y]==image[x][y] and not visited[x+1][y] :
                # image[x+1][y] = color
                q.append((x+1,y))
            if y-1>=0 and image[x][y-1]==image[x][y] and not visited[x][y-1]:
                # image[x][y-1] = color
                q.append((x,y-1))
            if y+1<c and image[x][y+1]==image[x][y] and not visited[x][y+1]:
                # image[x][y+1] = color
                q.append((x,y+1))
                
            image[x][y]=color
            visited[x][y]=True
            
        return image
