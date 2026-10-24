class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left-=1
                right+=1
            return left+1, right-1

        mxL = 0
        mxR = 0
        ans = 0

        for i in range(len(s)):
            l,r = expand(i, i) #odd palindrome
            if r-l+1>ans:
                ans = r-l+1
                mxL = l
                mxR = r

            l,r = expand(i, i + 1) #even palindrom
            if r-l+1>ans:
                ans = r-l+1
                mxL = l
                mxR = r
        
        return s[mxL:mxR+1]