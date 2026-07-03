from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # d = Counter(nums)
        # for k, v in d.items():
        #     if v>len(nums)//2:
        #         return k

        # Boyer-Moore Voting Algorithm
        res=count=0
        for num in nums:
            if count == 0:
                res = num

            if num == res:
                count += 1
            else:
                count -= 1
        return res

        
        


