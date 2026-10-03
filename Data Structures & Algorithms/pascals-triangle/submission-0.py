class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = [[1]]
        for i in range(numRows - 1):
            ans.append([1])
            for j in range(len(ans[-2]) - 1):
                num = ans[-2][j] + ans[-2][j + 1]
                ans[-1].append(num)
            ans[-1].append(1)
        return ans