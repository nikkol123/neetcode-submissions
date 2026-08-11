"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        hash_nodes = {None: None} # {key : [next, random]}
        
        cur = head
        while cur:
            hash_nodes[cur] = Node(cur.val)
            cur = cur.next

        cur = head
        dummy = hash_nodes[cur]
        while cur:
            hash_nodes[cur].next = hash_nodes[cur.next]
            hash_nodes[cur].random = hash_nodes[cur.random]
            cur = cur.next
        return dummy



