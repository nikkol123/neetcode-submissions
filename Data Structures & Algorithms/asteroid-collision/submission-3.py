class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for asteroid in asteroids:
            while stack and stack[-1] > 0 and asteroid < 0:
                if abs(stack[-1])<abs(asteroid):
                    stack.pop()
                    continue
                elif stack[-1] * asteroid < 0 and abs(asteroid) == abs(stack[-1]):
                    #shouldn't append after in this case
                    stack.pop()
                break
            else:
                stack.append(asteroid)
        return stack



        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        stack = []
        for asteroid in asteroids:
            while stack and stack[-1] > 0 and asteroid < 0:
                if abs(stack[-1]) < abs(asteroid):
                    stack.pop()
                    continue
                elif abs(stack[-1]) == abs(asteroid):
                    stack.pop()
                break
            else:
                stack.append(asteroid)
        return stack
