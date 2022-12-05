class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        c=0
        for i in matrix:
            for j in i:
                if j==target:
                    c+=1
                    break
        if(c>0):
            return True
        return False     
        