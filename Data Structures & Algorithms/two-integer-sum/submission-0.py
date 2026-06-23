class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i in range(len(nums)):
            if dic.get(target-nums[i]) != None:
                return [dic[target-nums[i]], i]
            dic.update({nums[i]: i})
