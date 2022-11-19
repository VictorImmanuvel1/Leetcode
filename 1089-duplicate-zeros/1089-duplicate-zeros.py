class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        for i in range(len(arr)):
            if(arr[i]==0):
                arr.insert(i+1,"")
                arr.pop()
            if(arr[i]==""):
                arr[i]=0