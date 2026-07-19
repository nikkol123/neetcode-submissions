class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] #pair [value, index]
        res = [0] * len(temperatures)
        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                t_prev, i_prev = stack.pop()
                res[i_prev] = i - i_prev
            stack.append([t, i])
        return res

            
        

