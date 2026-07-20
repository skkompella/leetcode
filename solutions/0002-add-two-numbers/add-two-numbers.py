# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        head = ListNode()
        dummy = head
        
        while l1 != None or l2 != None or carry != 0:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            v = 0
            s = v2 + v1 + carry
            if s >= 10:
                carry = s//10
                v = s%10
            else:
                carry=0
                v = s
            
            
            head.next = ListNode()
            head = head.next
            head.val = v
            if l1:
                l1=l1.next
            if l2:
                l2=l2.next
        
        return dummy.next
