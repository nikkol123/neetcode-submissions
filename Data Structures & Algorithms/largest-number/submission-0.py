class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = [str(num) for num in nums]

        nums.sort(key=lambda num: num * 10, reverse=True)

        return "0" if nums[0] == "0" else "".join(nums)