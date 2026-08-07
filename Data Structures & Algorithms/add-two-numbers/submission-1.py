# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        def Linked_to_Num(head):
            count = 0
            cur = head
            num = 0
            while cur:
                power = 10 ** count
                num += cur.val * power
                count += 1
                cur = cur.next
            return num

        num3 = Linked_to_Num(l1) + Linked_to_Num(l2)
        print(num3)
        
        if num3 == 0:
            return ListNode(0)

        dummy = ListNode()
        cur = dummy
        while num3:
            digit = num3 % 10
            cur.next = ListNode(digit)
            num3 = num3 // 10
            cur = cur.next
    
        return dummy.next
