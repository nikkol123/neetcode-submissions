class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0

        for target in set(s):
            for i in range(len(s)):
                replacements = k
                currentLen = 0

                for j in range(i, len(s)):
                    if s[j] != target:
                        if replacements == 0:
                            break
                        replacements -= 1

                    currentLen += 1
                    longest = max(longest, currentLen)

        return longest
