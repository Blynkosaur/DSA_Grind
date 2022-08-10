class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int):
        q = deque()
        original = image[sr][sc]
        q.append((sr,sc))
        visited = [(sr,sc)]
        while len(q) != 0:
            coord = q.popleft()
            x = coord[0]
            y = coord[1]
            if x-1>=0 and (x-1,y) not in visited and image[x-1][y]== original:
                q.append((x-1,y))
                visited.append((x-1,y))
            if x+1 <len(image) and (x+1,y) not in visited and image[x+1][y]== original:
                q.append((x+1,y))
                visited.append((x-1,y))
            if y+1 <len(image[0]) and (x,y+1) not in visited and image[x][y+1]== original:
                q.append((x,y+1))
                visited.append((x,y+1))
            if y-1 >=0and (x,y-1) not in visited and image[x][y-1]== original:
                q.append((x,y-1))
                visited.append((x,y-1))
            image[x][y]= color
        return image
        
        