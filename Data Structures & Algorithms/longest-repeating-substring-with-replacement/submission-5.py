from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counter = defaultdict(int)
        res = 0

        l = 0
        maxF = 0 #the char with the maximum value
        for right in range(len(s)):
            counter[s[right]] += 1
            maxF = max(maxF, counter[s[right]])

            while right - l + 1 - maxF > k:
                counter[s[l]] -= 1
                l += 1
            res = max(res, right - l + 1)

        return res