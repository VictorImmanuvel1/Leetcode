class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        b=[]
        for i in nums:
            if i not in b:
                b.append(i)
        nums.clear()
        for i in b:
            nums.append(i)
        return(len(nums))