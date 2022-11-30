class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        a=list(set(arr))
        b=[]
        for i in a:
            b.append(arr.count(i))
        return(len(b)==len(list(set(b))))
        
        