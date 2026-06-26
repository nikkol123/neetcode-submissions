class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out = [0] * len(nums)
        prod=1
        zeroCount=0
        #computing the total product
        for num in nums:
            if num:
                prod *= num
            else:
                prod *= num
                zeroCount+=1
        if zeroCount > 1:
            return [0]*len(nums)
        
        for i in range(len(nums)):
            if nums[i] != 0:
                out[i] = prod // nums[i]
            else:
                newProd=1
                for num in nums:
                    if num!=0:
                        newProd *= num
                out[i] = newProd
        return out