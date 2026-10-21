class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        directions = [[-1, 0], [1, 0], [0, 1], [0,-1] ]

        # i would union it only when there is 
        par = {}
        rank = {}

        def find(n):
            p = n
            while p != par[p]:
                par[p] = par[par[p]]
                p = par[p]
        
            return p
        
        def union (n1, n2):
            p1, p2 = find(n1), find(n2)

            if rank[p1] > rank[p2]:
                par[p2] = p1
            elif rank[p1] < rank [p2]:
                par[p1] = p2
		
            else:
                par[p1] = p2

                rank[p2] += 1 			
            return True
        numberOfIslands = 0

        res = []
        for x, y in positions:
            if (x,y) in par:
                res.append(numberOfIslands)
                continue
            par[(x,y)] = (x,y)
            rank[(x,y)] = 0
            numberOfIslands += 1
            for dr, dc in directions:
                nx, ny = x + dc, y + dr

                if (nx, ny) in par:
                    union((nx,ny), (x,y))
                    numberOfIslands -= 1
                    
                #just an addition
                #  
            if numberOfIslands < 1:
                numberOfIslands = 1 
            res.append(numberOfIslands)

        print(par)
        return res