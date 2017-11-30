# coding=utf-8

#o(n)的manacher就不做了。。。
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        start = 0
        max_len = 0
        i = len(s) / 2
        while i >= 0 and (i + 1) * 2 > max_len:
            max_, start_ = self.find1(s, i)
            if max_ > max_len:
                max_len = max_
                start = start_
            max_, start_ = self.find2(s, i)
            if max_ > max_len:
                max_len = max_
                start = start_
            i -= 1
        i = len(s) / 2 + 1
        while i < len(s) and (len(s) - i) * 2 - 1 > max_len:
            max_, start_ = self.find1(s, i)
            if max_ > max_len:
                max_len = max_
                start = start_
            max_, start_ = self.find2(s, i)
            if max_ > max_len:
                max_len = max_
                start = start_
            i += 1
        return s[start:start + max_len]

    def find1(self, s, mid):
        """
        :type s: str
        :type mid: int
        :rtype: list
        """
        max_len = -1
        start, end = mid, mid
        while start >= 0 and end < len(s) and s[start] == s[end]:
            max_len += 2
            start -= 1
            end += 1
        return [max_len, start + 1]

    def find2(self, s, mid):
        """
        :type s: str
        :type mid: int
        :rtype: list
        """
        max_len = 0
        start, end = mid, mid + 1
        while start >= 0 and end < len(s) and s[start] == s[end]:
            max_len += 2
            start -= 1
            end += 1
        return [max_len, start + 1]


if __name__ == '__main__':
    sol = Solution()
    print sol.longestPalindrome('babad')
    print sol.longestPalindrome('cbbd')
