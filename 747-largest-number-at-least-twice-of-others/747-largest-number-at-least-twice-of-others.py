class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        a=sorted(nums)
        if(a[-1]>=a[-2]*2):
            return(nums.index(a[-1]))
        else:
            return(-1)
        