class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        out = ""
        first = strs[0]
        last = strs[-1]
        print(sorted(strs))
        for i in range(len(min(first, last))):
            if first[i] == last[i]:
                out += first[i]
            else:
                break
        return out
