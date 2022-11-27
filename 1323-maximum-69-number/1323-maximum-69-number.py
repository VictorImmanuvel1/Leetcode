class Solution:
    def maximum69Number (self, num: int) -> int:
        b=list(str(num))
        for i in range(len(b)):
            if b[i]=="6":
                b[i]="9"
                break
        return(int("".join(b)))
        