class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # k = len(nums)
        # i=0
        # while i < len(nums):
        #     if nums[i]==val:
        #         nums.pop(i)
        #         k-=1
        #         i = i-1
        #     i+=1
        # return k

        k=0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k+=1
        return k


        
