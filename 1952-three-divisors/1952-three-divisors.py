class Solution:
    def isThree(self, n: int) -> bool:
        a=[i for i in range(1,n+1) if n%i==0]
        return len(a)==3
        
            