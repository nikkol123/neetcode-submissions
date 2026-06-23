class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # redC = 0
        # whiteC = 0
        # blueC = 0
        # for colour in nums:
        #     if colour == 0: redC+=1
        #     elif colour == 1: whiteC+=1
        #     elif colour == 2: blueC+=1 

        # index=0
        # while redC>0:
        #     nums[index]=0
        #     redC-=1
        #     index+=1
        # while whiteC>0:
        #     nums[index]=1
        #     index+=1
        #     whiteC-=1
        # while blueC>0:
        #     nums[index]=2
        #     index+=1
        #     blueC-=1

        left = 0
        mid = 0
        right = len(nums)-1

        while mid <= right:
            if nums[mid] == 0:
                nums[left], nums[mid] = nums[mid], nums[left]
                left += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            elif nums[mid] == 2:
                nums[mid], nums[right] = nums[right], nums[mid]
                right -= 1
            


    

            
                




        