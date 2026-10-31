from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        duplicates = Counter(s)
        for i, char in enumerate(s):
            if duplicates[char] == 1:
                return i
        return -1
