# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        final = ListNode()
        head = final
        carry = 0
        while l1 or l2 or carry:
            a = l1.val if l1 else 0
            b = l2.val if l2 else 0

            fin = a+b+carry

            carry = fin // 10  
            fin = fin % 10  

            head.next = ListNode(fin)

            head = head.next


            if l1: l1 = l1.next
            if l2: l2 = l2.next

        return final.next

        

            

