class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #brute force
        # result = [0] * len(temperatures)
        # for i in range(len(temperatures)-1):
        #     for j in range(i+1, len(temperatures)):
        #         if temperatures[j] > temperatures[i]:
        #             result[i] = j-i
        #             break
        # return result

        result = [0] * len(temperatures)
        stack = [] # (val, index)
        for i in range(len(temperatures)):
            while stack and temperatures[i] > stack[-1][0]:
                _, idx = stack.pop()
                result[idx] = i - idx
            stack.append((temperatures[i], i))

        return result
































        # stack = [] #pair [value, index]
        # res = [0] * len(temperatures)
        # for i, t in enumerate(temperatures):
        #     while stack and t > stack[-1][0]:
        #         t_prev, i_prev = stack.pop()
        #         res[i_prev] = i - i_prev
        #     stack.append([t, i])
        # return res

            
        

