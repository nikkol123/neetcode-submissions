from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # counter = Counter(nums)
        # out=[]
        # temp = counter.most_common(k)
        # for num in temp:
        #     out.append(num[0])
        # return out

        # counter with get for setting default values. 
        # for num in nums:
        #     count[num] = 1+count.get(num, 0)


        counter = {}
        freq = [[] for i in range(len(nums) + 1)]
        out = []

        for num in nums:
            if num in counter:
                counter[num]+=1
            else:
                counter[num]=1

        for key, value in counter.items():
            freq[value].append(key)

        index = len(freq)-1
        while k > 0:
            print(k)
            if freq[index]:
                out.append(freq[index].pop())
                k-=1
            else:
                index -= 1
        return out





        

        

        