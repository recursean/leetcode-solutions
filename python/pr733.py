class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:    
        if image[sr][sc] != color:
            self.dfs(image, sr, sc, image[sr][sc], color)
        return image
    
    def dfs(self, image, sr, sc, tgt, color):
        image[sr][sc] = color
        
        for i in range(4):
            cr = sr
            cc = sc
            # top
            if i == 0 and cr != 0:
                cr -= 1
            # bottom
            elif i == 1 and cr != len(image)-1:
                cr += 1
            # left
            elif i == 2 and cc != 0:
                cc -= 1
            # right
            elif i == 3 and cc != len(image[0])-1:
                cc += 1

            if image[cr][cc] == tgt:
                self.dfs(image, cr, cc, tgt, color)
