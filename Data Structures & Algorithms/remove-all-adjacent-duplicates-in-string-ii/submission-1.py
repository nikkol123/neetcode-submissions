class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []  # [char, count]

        for char in s:
            if stack and char == stack[-1][0]:
                stack[-1][1] += 1
            else:
                stack.append([char, 1])

            if stack[-1][1] == k:
                stack.pop()

        out = []
        for i in stack:
            while i[1] > 0:
                out.append(i[0])
                i[1] -= 1

        return "".join(out)

            