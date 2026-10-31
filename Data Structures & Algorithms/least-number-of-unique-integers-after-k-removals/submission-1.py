from collections import Counter
class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        freq = Counter(arr)
        seen = set(arr)
        sorted_freq = dict(sorted(freq.items(), key=lambda item: item[1]))
        for key,val in sorted_freq.items():
            if k >= val:
                k -= val
                seen.remove(key)
        return len(seen)
        
        

                    


