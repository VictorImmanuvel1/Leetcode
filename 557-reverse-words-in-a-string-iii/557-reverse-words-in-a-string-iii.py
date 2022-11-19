class Solution:
    def reverseWords(self, s: str) -> str:
        s=s.split()
        b=[]
        for i in s:
            b.append(i[::-1])
        return(" ".join(b))
        