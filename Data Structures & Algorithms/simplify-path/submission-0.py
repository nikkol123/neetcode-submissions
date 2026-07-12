class Solution:
    def simplifyPath(self, path: str) -> str:
        # if .. go back
        # if go back at the root node result in a root node
        parts = path.split("/")
        stack = []

        for part in parts:
            if part == "" or part == ".":
                continue
            elif part == "..":
                if stack: stack.pop()
            else: 
                stack.append(part)

        return "/" + "/".join(stack)