# coding=utf-8

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        while len(lists) > 1:
            temp = []
            for i in xrange(0, len(lists), 2):
                if i + 1 < len(lists):
                    merged = self.merge2Lists(lists[i], lists[i + 1])
                    temp.append(merged)
            if len(lists) % 2 == 1:
                temp.append(lists[-1])
            lists = temp
        return lists[0] if len(lists) > 0 else None

    def merge2Lists(self, list1, list2):
        """
        :type list1: ListNode
        :type list2: ListNode
        :rtype: ListNode
        """
        head = None
        tail = None
        while list1 or list2:
            if not list2:
                choose = list1
                list1 = list1.next
            elif not list1:
                choose = list2
                list2 = list2.next
            else:
                if list1.val <= list2.val:
                    choose = list1
                    list1 = list1.next
                else:
                    choose = list2
                    list2 = list2.next
            if not head:
                head = choose
            if tail:
                tail.next = choose
            tail = choose
        return head


if __name__ == '__main__':
    s = Solution()
    # print s.mergeKLists([[1],[1]])
