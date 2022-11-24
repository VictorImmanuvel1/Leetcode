class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        b=[]
        c=[]
        d=[]
        for i in range(len(nums)):
            if(nums[i]>0):
                b.append(nums[i])
            else:
                c.append(nums[i])
        for i in range(len(b)):
            d.append(b[i])
            d.append(c[i])
        return d
        