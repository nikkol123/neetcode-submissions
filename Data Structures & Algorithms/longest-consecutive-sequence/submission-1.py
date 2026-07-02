from collections import defaultdict
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        d = defaultdict(int)
        currentLongest = 1

        if not nums:
            return 0
        for num in nums:
            d[num]+=1

        for num in nums:
            current=1
            for i in range(len(nums)):
                if num+1 in d:
                    num+=1
                    current+=1
            if current>currentLongest:
                currentLongest = current

        return currentLongest
