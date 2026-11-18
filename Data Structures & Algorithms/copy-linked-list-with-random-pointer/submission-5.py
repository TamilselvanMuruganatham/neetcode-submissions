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
        if not head:
            return None
        nodes_dict={}
        curr=head
        while curr:
            nodes_dict[curr]=Node(curr.val)
            curr=curr.next
        curr=head
        while curr:
            copy_node=nodes_dict.get(curr)
            copy_node.next=nodes_dict.get(curr.next)
            copy_node.random=nodes_dict.get(curr.random)
            curr=curr.next
        return nodes_dict[head]