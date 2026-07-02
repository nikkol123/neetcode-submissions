class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # d = set()
        # currentLongest = 1

        # if not nums:
        #     return 0

        # for num in nums:
        #     d.add(num)

        # for num in nums:
        #     current=1
        #     for i in range(len(nums)):
        #         if num+1 in d:
        #             num+=1
        #             current+=1
        #     if current>currentLongest:
        #         currentLongest = current

        # return currentLongest

        d = set()
        out = 1
        if not nums:
            return 0

        for num in nums:
            d.add(num)
        
        for num in d:
            if num-1 not in d:
                current = 1
                while num+1 in d:
                    current+=1
                    num+=1
                if current>out: out = current

        return out
        


