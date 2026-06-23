from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        table = Counter(nums)
        print(table)
        for k, v in table.items():
            if v > len(nums)//2:
                return k