class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # capacity (cap) is how much weight can a ship take at a time
        # since if days == 1, then r must be the sum to make all in 1 go
        l, r = max(weights), sum(weights)

        def canShip(cap):
            d = 1
            currentWeight = 0
            for weight in weights:
                if currentWeight + weight > cap:
                    d+=1
                    currentWeight = 0
                currentWeight += weight 
            return d <= days 


        while l<=r:
            cap = (l+r)//2
            if canShip(cap): r = cap - 1
            else: l = cap + 1
        return l