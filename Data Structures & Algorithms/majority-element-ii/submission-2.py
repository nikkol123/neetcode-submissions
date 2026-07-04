from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        top1 = top2 = None
        freq1 = freq2 = 0
        out=[]
        for num in nums:
            if freq1 == 0:
                top1 = num
            if freq2 == 0:
                top2 = num

            if num == top1:
                freq1+=1
            elif num == top2:
                freq2+=1
            else:
                freq1-=1
                freq2-=1
        
        count1 = count2 =0
        for num in nums:
            if num == top1: count1+=1
            if num == top2: count2+=1
        if count1>len(nums)//3: out.append(top1)
        if count2>len(nums)//3 and top2!=top1: out.append(top2)
        return out


            
                