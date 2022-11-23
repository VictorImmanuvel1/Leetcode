class Solution:
    def removeStars(self, s: str) -> str:
        st=[]
        for i in s:
            if(len(st)>0 and i=='*'):
                st.pop()
            else:
                st.append(i)
        return("".join(st))
        