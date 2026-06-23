class Solution:

    def encode(self, strs: List[str]) -> str:
        out = ""
        for string in strs:
            out += str(len(string)) + "#" + string
        print(out)
        return out

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



