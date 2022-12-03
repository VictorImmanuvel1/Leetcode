class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        a=-1
        for i in s:
            if s.count(i)==1:
                a=s.index(i)
                break
        return a
        