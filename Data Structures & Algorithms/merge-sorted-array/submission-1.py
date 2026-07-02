class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        left1 = m - 1
        left2 = n - 1
        right = m + n - 1
        temp = 0
        while left2>=0:
            if left1>=0:
                temp=nums1[left1]
            else:
                temp = float('-inf')
            if temp<nums2[left2]:
                nums1[right] = nums2[left2]
                left2 -= 1
            else:
                nums1[right] = temp
                left1 -= 1
            right -= 1



        