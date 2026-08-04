class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        l_s, l_t = 0, 0
        fine = []
        mini = min(len(s), len(t))
        while l_s < len(s) and l_t < len(t):
            if t[l_t] == s[l_s]:
                fine.append(s[l_s])
                l_t += 1
            l_s += 1

        return len(t) - len(fine)
            
