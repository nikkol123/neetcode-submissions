class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        out = []
        l1, l2 = 0, 0

        while l1 < len(word1) and l2 < len(word2):
            out.append(word1[l1])
            out.append(word2[l2])
            l1+=1
            l2+=1
        out.append(word1[l1:])
        out.append(word2[l2:])

        return "".join(out)
