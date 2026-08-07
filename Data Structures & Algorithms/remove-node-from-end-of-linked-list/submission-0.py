# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cur = head
        length = 0
        while cur:
            cur = cur.next
            length+=1
        
        index = length - n

        if index == 0:
            return head.next

        cur = head
        count = 1
        while cur:
            if count == index:
                cur.next = cur.next.next
                break
            cur = cur.next
            count += 1
        return head
