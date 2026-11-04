# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        index1=index2=1
        num1=num2=0
        while l1:
            num1 +=  l1.val*index1
            index1 *= 10
            l1=l1.next
        while l2:
            num2 +=  l2.val*index2
            index2 *= 10
            l2=l2.next
        summ=num1+num2
        node=ListNode()
        dummy=node
        if not summ:
            return ListNode()
        while summ:
            val = summ%10
            summ //= 10
            new_node=ListNode(val)
            node.next=new_node
            node=node.next
        return dummy.next


        

    
            
        