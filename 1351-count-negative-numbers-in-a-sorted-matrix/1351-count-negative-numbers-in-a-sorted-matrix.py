class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        b=0
        for i in grid:
            for j in i:
                if(j<0):
                    b+=1
        return b
        