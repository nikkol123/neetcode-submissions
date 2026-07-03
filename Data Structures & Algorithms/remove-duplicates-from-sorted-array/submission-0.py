class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k, left = 1, 0
        while left<len(nums)-1:
            if nums[left]!=nums[left+1]:
                nums[k] = nums[left+1]
                k+=1
            left+=1
        return k