class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        #Brute Force

        # res = float("inf")
        # for i in range(len(nums)):
        #     localSum = 0
        #     for j in range(i, len(nums)):
        #         localSum += nums[j]
        #         if localSum >= target:
        #             res = min(res, j - i +1)
        #             break
        
        
        res = float("+inf")
        l = 0
        localSum = 0


        for right in range(len(nums)):
            localSum += nums[right]
            while localSum >= target:
                res = min(res, right-l+1)
                localSum -= nums[l]
                l+=1

        if res == float("+inf"): return 0
        else: return res