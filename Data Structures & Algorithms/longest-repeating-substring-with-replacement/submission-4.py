from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counter = defaultdict(int)
        left = 0
        max_freq = 0
        result = 0

        for right in range(len(s)):
            counter[s[right]] += 1

            max_freq = max(max_freq, counter[s[right]])

            window_length = right - left + 1

            while window_length - max_freq > k:
                counter[s[left]] -= 1
                left += 1
                window_length = right - left + 1

            result = max(result, right - left + 1)

        return result