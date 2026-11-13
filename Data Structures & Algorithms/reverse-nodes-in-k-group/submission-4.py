# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy=ListNode()
        dummy.next=head
        prev_group_node=dummy

        while True:
            kth_node=head
            for _ in range(k-1):
                if not kth_node:break
                kth_node=kth_node.next
            if not kth_node:
                break
            
            next_group_node=kth_node.next
            prev_node=next_group_node
            current_node=head
            while current_node != next_group_node:
                new_node=current_node.next
                current_node.next=prev_node
                prev_node=current_node
                current_node=new_node
            
            prev_group_node.next=kth_node
            prev_group_node=head
            head=next_group_node

        return dummy.next





