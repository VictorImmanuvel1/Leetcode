class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        b=[]
        c=0
        while(len(nums)!=0):
            c=(min(nums)+max(nums))/2
            b.append(c)
            nums.remove(min(nums))
            nums.remove(max(nums))
            c=0
        return len(set(b))   
        