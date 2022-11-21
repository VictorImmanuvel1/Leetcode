class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if(dividend==-2147483648 and divisor==-1):
            return((abs(dividend)//abs(divisor)-1))
        elif(dividend<0 and divisor<0):
            return((abs(dividend)//abs(divisor)))
        elif(dividend<0 or divisor<0):
            return((abs(dividend)//abs(divisor))*-1)
        else:
            return dividend//divisor
        