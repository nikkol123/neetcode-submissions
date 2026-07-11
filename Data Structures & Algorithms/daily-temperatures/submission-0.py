class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        for i in range(len(temperatures)):
            count = 1
            for j in range(i+1, len(temperatures)):
                if temperatures[j]>temperatures[i]:
                    result[i] = count
                    break
                else: count+=1
        return result


