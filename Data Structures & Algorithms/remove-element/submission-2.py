class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = len(nums)
        i=0
        while i < len(nums):
            if nums[i]==val:
                nums.pop(i)
                k-=1
                i = i-1
            i+=1
        print(nums)
        return k

        
