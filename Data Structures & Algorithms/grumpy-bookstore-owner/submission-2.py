class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        l = 0
        basic_sum = 0
        current_window, max_window = 0, 0
        for r in range(len(customers)):
            if grumpy[r]:
                current_window += customers[r]
            else:
                basic_sum += customers[r]
            
            if r-l+1>minutes:
                if grumpy[l]:
                    current_window-=customers[l]
                l+=1
            max_window = max(max_window, current_window)
        return basic_sum+max_window
