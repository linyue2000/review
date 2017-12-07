#coding=utf-8

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        pre = None
        p1 = head
        head = p1.next
        while p1 and p1.next:
            p2 = p1.next
            p1.next = p2.next
            p2.next = p1
            if pre:
                pre.next = p2
            pre = p1
            p1 = p1.next
        return head


if __name__ == '__main__':
    pass