class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if(nums[i]>0 and nums[i]<10):
                nums.append(nums[i])
            elif(nums[i]>=10):
                a=list(str(nums[i]))
                a=a[::-1]
                a="".join(a)
                nums.append(int(a))
            else:
                a=list(str(abs(nums[i])))
                a=a[::-1]
                a="".join(a)
                nums.append(int(a)-(2*int(a)))
        return(len(list(set(nums))))
        