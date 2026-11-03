# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        nodes=[]
        node=head
        while node:
            nodes.append(node)
            node=node.next
        start=0
        end=len(nodes)-1
        while start<end:
            nodes[start].next=nodes[end]
            start+=1
            if start==end:
                break
            nodes[end].next=nodes[start]
            end-=1
        nodes[start].next=None
        

    