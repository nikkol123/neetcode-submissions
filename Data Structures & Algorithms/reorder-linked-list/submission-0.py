# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        length = 0
        cur = head

        while cur:
            cur = cur.next
            length += 1

        mid = (length + 1) //2

        cur = head
        prev = None
        last = head
        index = 0
        print("2")

        while cur:
            temp = cur.next

            if index < mid:
                last = cur       # Last node of the first half
            else:
                cur.next = prev
                prev = cur

            cur = temp
            index += 1

        last.next = None 

        print("3")

        cur1 = head
        cur2 = prev
        while cur2:
            first_next = cur1.next
            second_next = cur2.next

            cur1.next = cur2
            cur2.next = first_next

            cur1 = first_next
            cur2 = second_next