class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        # for counter in range(len(nums)*2):
        #     index = counter % len(nums)
        #     ans.append(nums[index])
        # return ans

        for i in range(2):
            for num in nums:
                ans.append(num)
        return ans
