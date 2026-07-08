class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        leftSize, leftChild = len(s)-1, len(g)-1
        out=0
        g.sort()
        s.sort()
        while leftSize >= 0 and leftChild >= 0:
            print(leftSize, leftChild)
            if s[leftSize] >= g[leftChild]:
                leftSize -= 1
                leftChild -= 1
                out+=1
            else:
                leftChild -= 1
        
        return out
        