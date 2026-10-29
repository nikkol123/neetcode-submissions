class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i, num in enumerate(nums):
            dic.update({num:i})
        for i, num in enumerate(nums):
            rem = target - num
            if rem in dic and dic[rem] != i: 
                return [min(i,dic[rem]), max(i,dic[rem])]
