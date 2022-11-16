class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        b=sorted(magazine)
        c=0
        for i in ransomNote:
            if i in b:
                c+=1
                b.remove(i)
        return c==len(ransomNote)
            
            
        
        
        