class Solution:

    def encode(self, strs: List[str]) -> str:
        parts = []
        for string in strs:
            parts.append(str(len(string)) + "#" + string) #   num+#+word

        return "".join(parts) # constant time

    def decode(self, s: str) -> List[str]:
        out = []
        i = 0

        while i < len(s):
            length = ""
            while s[i] != "#":
                length += s[i]
                i += 1
            length = int(length)
            i += 1  # skip "#"
            out.append(s[i:i + length])
            i += length
        return out



