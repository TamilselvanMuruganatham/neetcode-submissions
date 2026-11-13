# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy=ListNode()
        dummy.next=head
        right_node=dummy
        left_node=dummy
        count=0
        while right_node and count<=n:
            right_node=right_node.next
            count+=1
        while right_node:
            left_node=left_node.next
            right_node=right_node.next
        left_node.next=left_node.next.next
        return dummy.next
        