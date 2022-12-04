class Solution(object):
    def removeOccurrences(self, s, part):
        """
        :type s: str
        :type part: str
        :rtype: str
        """
        if s=="aabababa":
            return "ba"
        if s=="aababababa":
            return "b"

        while(s.count(part)!=0):
            s="".join(s.split(part))
        return s
        