class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights)-1
        max_volume = 0
        while left < right:
            volume = min(heights[left], heights[right]) * (right - left)
            max_volume = max(max_volume, volume)
            if heights[left] < heights[right]:
                left += 1
            else:
                right -=1
        return max_volume



























        # left, right = 0, len(heights) - 1
        # maximum = 0
        # while left < right:
        #     smaller = min(heights[left], heights[right])
        #     area = (right - left) * smaller
        #     if area >= maximum:
        #         maximum = area
        #         print(left, right, area)
        #     if heights[right] == smaller: right -=1
        #     else: left+=1
   
        # return maximum
