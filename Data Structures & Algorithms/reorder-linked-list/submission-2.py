# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #store the nodes first and rebuild the linked list in the right order
        nodes = []
        cur = head

        while cur:
            nodes.append(cur)
            cur = cur.next
        
        left, right = 0, len(nodes)-1

        while left < right:
            nodes[left].next = nodes[right]
            left+=1
            if left<right:
                nodes[right].next = None
            nodes[right].next = nodes[left]
            right -= 1
        nodes[left].next = None

        1,2,3,4
        1,2,3