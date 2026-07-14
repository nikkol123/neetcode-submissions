class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r = 1, max(piles) + 1
        while l<=r:
            k = (l+r)//2
            hours = 0
            for pile in piles:
                hours += (pile + k - 1) // k

            if hours > h:
                l = k+1
            else: 
                r = k-1
        return l