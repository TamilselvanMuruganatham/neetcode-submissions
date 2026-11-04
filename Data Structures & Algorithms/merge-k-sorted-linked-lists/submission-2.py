# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq as hq
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        nodes_list=[]
        i=0
        for node in lists:
            if node:
                hq.heappush(nodes_list,(node.val,i,node))
            i+=1
        dummy_node=ListNode()
        node=dummy_node
        while nodes_list:
            _,i,min_node=hq.heappop(nodes_list)
            node.next=min_node
            node=node.next

            if min_node.next:
                min_node=min_node.next
                hq.heappush(nodes_list,(min_node.val,i,min_node))
        return dummy_node.next




        