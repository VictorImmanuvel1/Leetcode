class Solution:
    def frequencySort(self, s: str) -> str:
        b=sorted(list(set(s)))
        a=[]
        for i in range(len(b)):
            if b[i] in s:
                a.append(b[i]*s.count(b[i]))
        c = sorted(a, key=len)
        return("".join(c[::-1]))
        