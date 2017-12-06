# coding=utf-8

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        p1, p2 = l1, l2
        head = None
        tail = None
        while p1 or p2:
            if p1 and not p2:
                choose = p1
                p1 = p1.next
            elif not p1 and p2:
                choose = p2
                p2 = p2.next
            else:
                if p1.val <= p2.val:
                    choose = p1
                    p1 = p1.next
                else:
                    choose = p2
                    p2 = p2.next
            if not head:
                head = choose
            if not tail:
                tail = choose
            else:
                tail.next = choose
                tail = tail.next
        return head


