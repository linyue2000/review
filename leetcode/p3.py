# coding=utf-8

# class Solution(object):
#     def lengthOfLongestSubstring(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
#         i, j = 0, 0
#         dmap = {}
#         max_len = 0
#         while j < len(s):
#             d = s[j]
#             if d in dmap:
#                 max_len = max(max_len, (j - 1) - i + 1)
#                 occur = dmap[d]
#                 for k in xrange(i, occur + 1):
#                     del dmap[s[k]]
#                 i = occur + 1
#             dmap[d] = j
#             j += 1
#         return max_len

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        i, j = 0, 0
        dmap = {}
        max_len = 0
        while j < len(s):
            d = s[j]
            if d in dmap and dmap[d] >= i:
                i = dmap[d] + 1
            max_len = max(max_len, j - i + 1)
            dmap[d] = j
            j += 1
        return max_len


if __name__ == '__main__':
    sol = Solution()
    print sol.lengthOfLongestSubstring("abc")
    print sol.lengthOfLongestSubstring("abcbde")
    print sol.lengthOfLongestSubstring("abcabcbb")
    print sol.lengthOfLongestSubstring("bbbbb")
    print sol.lengthOfLongestSubstring("pwwkew")
