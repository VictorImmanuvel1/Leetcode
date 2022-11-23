class Solution:
    def partitionString(self, s: str) -> int:
        a=''
        b=[]
        for i in s:
            if i not in a:
                a+=i
            else:
                b.append(a)
                a=i
        b.append(a)
        return len(b)
        