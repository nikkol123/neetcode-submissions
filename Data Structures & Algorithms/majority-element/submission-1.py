from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = Counter(nums)
        for k, v in d.items():
            if v>len(nums)//2:
                return k


















        # table = Counter(nums)
        # print(table)
        # for k, v in table.items():
        #     if v > len(nums)//2:
        #         return k
        


