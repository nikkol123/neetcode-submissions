class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        l, r = 0, minutes - 1
        res = 0
        while r < len(grumpy):
            local = 0
            for i in range(len(grumpy)):
                if i >=l and i<=r:
                    local += customers[i]
                elif not grumpy[i]:
                    local += customers[i]
            l+=1
            r+=1
            res = max(res, local)
        return res
            




