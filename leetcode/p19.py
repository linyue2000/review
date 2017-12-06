# coding=utf-8

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        list = []
        cur = head
        i = 0
        while cur:
            list.append(cur)
            cur = cur.next
            i += 1
        remove_index = i - n
        if remove_index == 0:
            return head.next
        else:
            list[remove_index - 1].next = list[remove_index].next
            return head


if __name__ == '__main__':
    sol = Solution()
    # print sol.removeNthFromEnd()
