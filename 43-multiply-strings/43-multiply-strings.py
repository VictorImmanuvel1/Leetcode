class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        r1 = 0
        r2 = 0
        for digit in num1:
            r1 *= 10
            for d in '0123456789':
                r1+=digit>d
        for digit in num2:
            r2 *= 10
            for d in '0123456789':
                r2+=digit>d
        return(str(r1*r2))