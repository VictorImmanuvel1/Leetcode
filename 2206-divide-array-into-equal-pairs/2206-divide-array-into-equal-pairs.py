class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        a=0
        for i in nums:
            if(nums.count(i)%2==0):
                a+=1
        return a==len(nums)
        