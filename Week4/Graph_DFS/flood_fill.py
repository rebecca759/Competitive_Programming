class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        color = image[sr][sc]
        
        if color == newColor:
            return image
        
        else:
            self.dfs(image,sr,sc,newColor,color)
        
        return image
        
    def dfs(self,image,r,c,newColor,color):
        if r < 0 or r > len(image)-1 or c < 0 or c > len(image[0])-1:
            return
        
        print(image)
        
        if (image[r][c] == color):
            image[r][c] = newColor       
            
            self.dfs(image,r+1,c,newColor,color)
            self.dfs(image,r-1,c,newColor,color)
            self.dfs(image,r,c+1,newColor,color)
            self.dfs(image,r,c-1,newColor,color)
