'''
You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
'''

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        carry = 0
        first = True
        head = ListNode(None)
    
        while l1 or l2 or carry:
            sum = carry
            if l1:
                sum+=l1.val
                l1 = l1.next
            if l2:
                sum+=l2.val
                l2 = l2.next
        
            val = sum%10
            carry = sum/10
        
            if first == True:
                head.val = val
                node = head
                first = False
            else:
                node.next = ListNode(val)
                node = node.next
        return head