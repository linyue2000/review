#coding=utf-8

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        pre = None
        p = head
        while p:
            nodes = []
            for i in xrange(0, k):
                if not p:
                    break
                nodes.append(p)
                p = p.next
            if len(nodes) == k:
                for i in xrange(len(nodes) - 1, 0, -1):
                    nodes[i].next = nodes[i - 1]
                nodes[0].next = p
                if pre:
                    pre.next = nodes[len(nodes) - 1]
                else:
                    head = nodes[len(nodes) - 1]
                pre = nodes[0]
            else:
                break
        return head


