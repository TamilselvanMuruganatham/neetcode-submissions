# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node=None
        while head:
            value,head=head.val,head.next
            new_node=ListNode(value)
            new_node.next=node
            node=new_node
        return node
            
