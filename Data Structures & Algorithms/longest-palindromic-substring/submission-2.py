class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left-=1
                right+=1
            return right - left - 1, s[left+1:right]

        ans = 0
        out = ""

        for i in range(len(s)):
            length, string = expand(i, i) #odd palindrome
            if length > ans:
                ans = length
                out = string

            length, string  = expand(i, i + 1) #even palindrom
            if length > ans:
                ans = length
                out = string

        return out