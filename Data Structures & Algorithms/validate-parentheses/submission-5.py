class Solution:
    def isValid(self, s: str) -> bool:
        out = []

        for char in s:
            if out:
                temp = out[-1]

                if (temp == "(" and char == ")") or \
                   (temp == "[" and char == "]") or \
                   (temp == "{" and char == "}"):
                    out.pop()
                else:
                    out.append(char)
            else:
                out.append(char)

        return not out



