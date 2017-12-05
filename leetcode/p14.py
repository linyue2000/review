# coding=utf-8

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ''
        result = ''
        flag = True
        i = 0
        first_str = strs[0]
        while flag and i < len(first_str):
            c = first_str[i]
            for j in xrange(1, len(strs)):
                s = strs[j]
                if i >= len(s) or s[i] != c:
                    flag = False
            if flag:
                result += c
            i += 1
        return result


if __name__ == '__main__':
    sol = Solution()
    print sol.longestCommonPrefix(['a', 'b'])
