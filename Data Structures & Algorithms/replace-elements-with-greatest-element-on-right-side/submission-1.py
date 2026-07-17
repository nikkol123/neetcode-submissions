class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        localmax = max(arr)
        for i in range(len(arr)-1):
            if arr[i] == localmax:
                localmax = max(arr[i+1:])
                arr[i] = localmax
            else:
                arr[i] = localmax
        arr[-1]=-1
        return arr
        