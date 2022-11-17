class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        a=0
        for i in words:
            if pref == i[:len(pref)]:
                a+=1
        return(a)
        