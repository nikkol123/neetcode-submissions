class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = set()
        l = 0
        out = 0
        for i in range(len(s)):
            while s[i] in chars:
                chars.remove(s[l])
                l += 1
            # out = len(chars) if len(chars)
            chars.add(s[i])
            if len(chars) > out: out=len(chars)
        return out
            