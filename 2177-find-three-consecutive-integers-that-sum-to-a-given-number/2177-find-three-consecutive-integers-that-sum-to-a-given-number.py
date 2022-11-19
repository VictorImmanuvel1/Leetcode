class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        b=[]
        c=0
        if(num%3==0):
            c=num//3
            b.append(c-1)
            b.append(c)
            b.append(c+1)
        return b