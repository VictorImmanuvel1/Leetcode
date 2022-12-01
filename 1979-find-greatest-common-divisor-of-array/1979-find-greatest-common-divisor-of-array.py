class Solution:
    def findGCD(self, nums: List[int]) -> int:
        a=[min(nums),max(nums)]
        b=[]
        for i in range(1,max(nums)+1):
            if (min(nums)%i==0) and (max(nums)%i==0):
                b.append(i)
        return max(b)
        