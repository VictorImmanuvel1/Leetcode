class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        a=0
        c=sorted(heights)
        b=[]
        for i in range(len(c)):
            if c[i] in heights:
                a=heights.index(c[i])
                b.append(names[a])
        return b[::-1]