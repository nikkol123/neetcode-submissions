from collections import Counter
from collections import defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_freq = Counter(s1)
        s2_freq = defaultdict(int)
        n = len(s1)
        
        if len(s1) > len(s2): return False

        for i in range(len(s2)):
            print(s2_freq)
            s2_freq[s2[i]] += 1
            if i >= n:
                s2_freq[s2[i-n]] -= 1
                if s2_freq[s2[i-n]] == 0:
                    del s2_freq[s2[i-n]]
            if s1_freq == s2_freq:
                return True
        return False