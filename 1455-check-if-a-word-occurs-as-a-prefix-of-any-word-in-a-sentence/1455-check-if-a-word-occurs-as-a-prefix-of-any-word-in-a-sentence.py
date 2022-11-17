class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        a=0
        sentence=sentence.split()
        for i in sentence:
            if i[:len(searchWord)]==searchWord:
                a=sentence.index(i)+1
                break
        if(a==0):
            a=-1
        return a
        