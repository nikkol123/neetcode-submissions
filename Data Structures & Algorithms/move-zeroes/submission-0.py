class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeros = 0
        for num in nums:
            if num == 0: zeros += 1
        
        left = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[left] = nums[i]
                left += 1 

        for i in range(len(nums)-zeros, len(nums)):
            nums[i] = 0

        return nums[i]


            