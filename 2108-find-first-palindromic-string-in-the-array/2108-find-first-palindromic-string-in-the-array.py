class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        a=''
        for i in words:
            if i=="".join(list(i[::-1])):
                a=i
                break
        return(a)
        