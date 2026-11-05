# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        nodes=[]
        node=head
        dummy_node=ListNode()
        new_node=dummy_node
        while node:
            nodes.append(node)
            node=node.next
        nodes.pop(-n)
        if nodes:
            nodes[-1].next=None
        for node in nodes:
            new_node.next=node
            new_node=new_node.next
        return dummy_node.next

        
        