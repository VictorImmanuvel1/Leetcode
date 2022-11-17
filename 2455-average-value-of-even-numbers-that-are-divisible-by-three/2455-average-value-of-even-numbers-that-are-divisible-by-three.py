class Solution:
    def averageValue(self, nums: List[int]) -> int:
        a=0
        b=0
        for i in nums:
            if(i%2==0):
                if(i%3==0):
                    a+=i
                    b+=1
        if(a==0):
            return(a)
        else:
            return(a//b)