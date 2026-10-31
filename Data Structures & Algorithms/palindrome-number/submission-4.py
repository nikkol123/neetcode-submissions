class Solution:
    def isPalindrome(self, x: int) -> bool:
        #wihtout converting to a string
        ln = 0

        if x < 0: return False

        num = x
        while num > 0:
            num //= 10
            ln += 1 

        while x > 0:
            l_digit = x // 10**(ln-1) % 10
            r_digit = x % 10
            print(ln, l_digit, r_digit)
            if l_digit != r_digit: return False
            x -= l_digit * 10**(ln-1)
            x //= 10
            ln -= 2
        return True

