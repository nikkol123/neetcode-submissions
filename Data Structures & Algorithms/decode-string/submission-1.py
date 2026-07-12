class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for char in s:
            if char == "]":
                sub = ""
                while stack[-1]!="[":
                    sub = stack.pop() + sub
                stack.pop()
                count = 0
                num = 0
                while stack and stack[-1].isnumeric():
                    num += int(stack.pop()) * (10**count)
                    count+=1
                stack.append(num*sub)
            else:
                stack.append(char)
 
        return "".join(stack)

            