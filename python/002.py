# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        header = ListNode(0)
        p = header
        p1, p2 = l1, l2
        carry = 0
        while p1 and p2:
            carry, num = divmod(p1.val + p2.val + carry, 10)
            p.next = ListNode(num)
            p = p.next
            p1 = p1.next
            p2 = p2.next

        while p1:
            carry, num = divmod(p1.val + carry, 10)
            p.next = ListNode(num)
            p = p.next
            p1 = p1.next

        while p2:
            carry, num = divmod(p2.val + carry, 10)
            p.next = ListNode(num)
            p = p.next
            p2 = p2.next

        if carry:
            p.next = ListNode(carry)

        return header.next
            
