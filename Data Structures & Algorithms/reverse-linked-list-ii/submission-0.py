# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(-1)
        dummy.next = head
        correct_left = dummy

        counter = 1

        #find the position of the node before the reversed window
        while counter < left:
            correct_left = correct_left.next
            counter += 1
        
        prev = None
        cur = correct_left.next
        remember = correct_left.next

        for _ in range(right - left + 1):
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp

        correct_left.next = prev
        remember.next = cur


        return dummy.next
        



            


        # correct_right