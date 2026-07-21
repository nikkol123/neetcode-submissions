# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        nodes = []
        cur = head
        while cur:
            nodes.append(cur)
            cur = cur.next

        left, right = 1, len(nodes)-1
        cur = head
        while left < right:
            cur.next = nodes[right]
            cur.next.next = nodes[left]

            left += 1
            right -= 1
            cur = cur.next.next

        if left == right:
            cur.next = nodes[left]
            cur = cur.next

        cur.next = None