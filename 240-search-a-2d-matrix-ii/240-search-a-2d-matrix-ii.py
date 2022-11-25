class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        c=0
        for i in matrix:
            for j in i:
                if j==target:
                    c+=1
                    break
        if(c>0):
            return True
        return False        