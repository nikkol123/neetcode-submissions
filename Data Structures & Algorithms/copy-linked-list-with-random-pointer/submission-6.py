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
        nodes = {}
        cur = head

        if not head:
            return None

        while cur:
            nodes[cur] = Node(cur.val)
            cur = cur.next

        deep_head = nodes[head]

        cur = head
        while cur:
            next_node = cur.next

            random_node = cur.random
            if not random_node: random_node = None

            if not next_node: nodes[cur].next = None
            else: nodes[cur].next = nodes[next_node]

            if not random_node: nodes[cur].random = None
            else: nodes[cur].random = nodes[random_node]

            cur = cur.next

        return deep_head

