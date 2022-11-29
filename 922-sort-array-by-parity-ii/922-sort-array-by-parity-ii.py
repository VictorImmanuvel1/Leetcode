class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        b=[i for i in nums if i%2!=0]
        c=[i for i in nums if i%2==0]
        d=2
        for i in range(len(nums)):
            if(i==1):
                c.insert(i,b[i-1])
            if(i!=1 and i%2!=0):
                c.insert(i,b[i-d])
                d+=1
        return c
        