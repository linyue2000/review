# coding=utf-8

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        for i in xrange(0, len(haystack) - len(needle) + 1):
            for j in xrange(0, len(needle)):
                if haystack[i + j] != needle[j]:
                    break
            else:
                return i
        return -1