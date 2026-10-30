# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev_node=None
        while head:
            new_node=ListNode(head.val)
            new_node.next=prev_node
            prev_node=new_node
            head=head.next
        return prev_node

            
