class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        freq = [0] * 2001
        for num in nums:
            idx = num + 1000
            freq[idx] += 1

        for pointer in range(2000, -1, -1):
            while k > 1 and freq[pointer] > 0:
                k-=1
                freq[pointer] -= 1

            if k == 1 and freq[pointer]: return pointer - 1000

        return 0