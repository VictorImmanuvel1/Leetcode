class Solution:
    def reverse(self, x: int) -> int:
        a=abs(x)
        b=0
        while(a!=0):
            c=a%10
            b=b*10+c
            a//=10
        if(x<0):
            b=b-(2*b)
        if abs(b) < 2**31 and b != 2**31 - 1:
            return b
        else:
            return 0
        