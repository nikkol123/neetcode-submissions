from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        d = Counter(nums)
        out=[]
        for k, v in d.items():
            if v>len(nums)//3:
                out.append(k)
        return out
                