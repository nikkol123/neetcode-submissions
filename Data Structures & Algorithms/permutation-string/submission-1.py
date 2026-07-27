from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        counter = Counter(s1)
        left = 0
        missing = len(s1)

        for right in range(len(s2)):
            right_char = s2[right]

            # Add right_char to the window
            if counter[right_char] > 0:
                missing -= 1

            counter[right_char] -= 1

            # Window is too large: remove its leftmost character
            if right - left + 1 > len(s1):
                left_char = s2[left]

                # It was a useful matched character
                if counter[left_char] >= 0:
                    missing += 1

                # Restore it because it leaves the window
                counter[left_char] += 1
                left += 1

            if missing == 0:
                return True

        return False