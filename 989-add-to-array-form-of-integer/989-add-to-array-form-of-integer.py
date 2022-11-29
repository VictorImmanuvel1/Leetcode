class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        s=[str(i) for i in num]
        b=int("".join(s))+k
        c=list(str(b))
        d=[int(i) for i in c]
        return d