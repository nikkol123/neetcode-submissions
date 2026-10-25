from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        COLS = len(grid[0])
        ROWS = len(grid)
        DIRECTIONS = [[1,0], [-1,0], [0,1], [0, -1]]
        

        #get all the treasures
        queue = deque()
        visited = set()
        for j in range(ROWS):
            for i in range(COLS):
                if grid[j][i] == 0:
                    queue.append((i,j))
                    visited.add((i,j))
        
        distance = 0 
        while queue:
      
            for _ in range(len(queue)):
                x, y = queue.popleft()
                grid[y][x] = distance

                for nc, nr in DIRECTIONS:
                    nx, ny = x + nc, nr + y
                    
                    if 0 <= nx < COLS and 0<= ny < ROWS and (nx, ny) not in visited:
                      
                        if grid[ny][nx] == 2 ** 31 - 1:
            
                            queue.append((nx, ny))
                            visited.add((nx, ny))
        
            distance += 1
        




        

