# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        nodes=[]
        node=head
        start,end=0,-1
        while node:
            end+=1
            nodes.append(node)
            node=node.next
        
        while start<end:
            nodes[start].next=nodes[end]
            start+=1
            nodes[end].next=nodes[start]
            end-=1
        nodes[start].next=None
    