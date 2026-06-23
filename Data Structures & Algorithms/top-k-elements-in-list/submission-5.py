from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        out=[]
        temp = counter.most_common(k)
        for num in temp:
            out.append(num[0])
        return out
        

        