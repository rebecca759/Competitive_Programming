class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        res = []
        
        for i in range(len(box)):
            free = False
            spots = deque()
            for j in range(len(box[0])-1,-1,-1):
                
                if free and box[i][j] == "#":
                    r,c = spots.popleft()
                    box[r][c] = "#"
                    box[i][j] = "."
                
                if box[i][j] == ".":
                    free = True
                    spots.append((i,j))
                    
                else:
                    if free:
                        spots = deque()
                    free = False
         
        for i in range(len(box[0])):
            res.append([])
            for j in range(len(box)-1,-1,-1):
                res[i].append(box[j][i])
      
        return res
