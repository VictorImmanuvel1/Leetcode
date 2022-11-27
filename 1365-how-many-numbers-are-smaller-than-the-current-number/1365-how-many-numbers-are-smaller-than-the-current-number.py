class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        b=[]
        c=0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if(nums[i]>nums[j]):
                    c+=1
            b.append(c)
            c=0
        return b
        