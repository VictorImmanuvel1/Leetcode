class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            if(nums[i]==nums[i-1]):
                nums[i-1]=nums[i-1]*2
                nums[i]=0
            if(nums[i]==0):
                nums.remove(nums[i])
                nums.extend([0])
        return nums
        