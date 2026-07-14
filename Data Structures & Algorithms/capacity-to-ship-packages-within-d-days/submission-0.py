class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # capacity (cap) is how much weight can a ship take at a time
        # since if days == 1, then r must be the sum to make all in 1 go
        l, r = max(weights), sum(weights)

        def canShip(cap):
            d = 1
            currentWeight = 0
            i = 0
            while i <= len(weights)-1:
                currentWeight += weights[i]
                if currentWeight > cap:
                    d += 1
                    currentWeight=0
                else:
                    i+=1

            if d > days: return False
            else: return True


        while l<=r:
            cap = (l+r)//2
            if canShip(cap): r = cap - 1
            else: l = cap + 1
        return l

        # weights=[1,5,4,4,2,3]
        # l = 5, r = 19, cap = 12
        # days=3
            