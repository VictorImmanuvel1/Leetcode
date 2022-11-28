class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        win,lose=zip(*matches)
        return([sorted(set(win)-set(lose)),sorted(k for k,l in Counter(lose).items() if l==1)])
        