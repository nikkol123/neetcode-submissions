class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l, r = 0, len(nums) - 1
        pointer = len(nums) -1
        out = [0] * len(nums)
        while l <= r:
            if abs(nums[l]) > abs(nums[r]):
                out[pointer] = nums[l]**2
                l += 1
            else:
                out[pointer] = nums[r] **2
                r -= 1
            pointer -=1

        return out
        









        # for i in range(len(nums)):
        #     nums[i] = nums[i] ** 2
        # return sorted(nums)
            