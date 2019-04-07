# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

def show(head):
    out = ""
    while head:
       out += " " + str(head.val)
       head = head.next
    print(out)

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        left = head
        middle = head.next
        left.next = None
        while middle.next is not None:
            temp = middle.next
            middle.next = left
            left = middle
            middle = temp
        middle.next = left
        return middle 
                

