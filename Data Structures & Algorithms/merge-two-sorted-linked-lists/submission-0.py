# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode()
        node=dummy
        while list1 and list2:
            list1_value, list2_value=list1.val,list2.val

            if list1_value<=list2_value:
                node.next=ListNode(list1_value)
                list1=list1.next

            else:
                node.next=ListNode(list2_value)
                list2=list2.next
            node=node.next
        while list1:
            node.next=ListNode(list1.val)
            node=node.next
            list1=list1.next
        while list2:
            node.next=ListNode(list2.val)
            node=node.next
            list2=list2.next
        return dummy.next
        


        