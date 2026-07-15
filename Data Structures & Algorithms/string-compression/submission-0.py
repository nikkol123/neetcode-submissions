class Solution:
    def compress(self, chars: List[str]) -> int:
        s = ""
        current = 1 #points to the current elemetn
        l = 0 #points to the position we will insert the compressed bit
        count=1
        while current < len(chars):
            if chars[current-1]==chars[current]:
                count += 1
            else:
                chars[l] = chars[current-1]
                l+=1
                if count != 1:
                    for digit in str(count):
                        chars[l] = digit
                        l+=1
                count=1
            current+=1
         # handle the final group
        chars[l] = chars[current - 1]
        l += 1

        if count != 1:
            for digit in str(count):
                chars[l] = digit
                l += 1
                
        return l