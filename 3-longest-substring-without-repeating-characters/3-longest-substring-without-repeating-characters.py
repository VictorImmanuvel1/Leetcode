class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        a=[]
        b=''
        c=[]
        d=0
        for i in s:
            if i not in a:
                a.append(i)
            else:
                b="".join(a)
                c.append(b)
                a.append(i)
                if(a.index(i)==0):
                    a=a[1:]
                else:
                    del a[:a.index(i)+1]
        c.append("".join(a))
        for i in c:
            if(len(i)>d):
                d=len(i)
        return d