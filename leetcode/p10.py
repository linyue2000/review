# coding=utf-8

class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        self.dp_init()
        return self.__is_match(s, p)

    def dp_init(self):
        self.dp = {}

    def dp_add(self, s, p, b):
        if s not in self.dp:
            self.dp[s] = {}
        self.dp[s][p] = b

    def dp_get(self, s, p):
        if s in self.dp and p in self.dp[s]:
            return self.dp[s][p]
        return None

    def __is_match(self, s, p):
        dp_cache = self.dp_get(s, p)
        if dp_cache is not None:
            return dp_cache
        if len(p) == 0:
            if len(s) == 0:
                self.dp_add(s, p, True)
                return True
            else:
                self.dp_add(s, p, False)
                return False
        j = 0
        c = p[j]
        j += 1
        more = False
        if j < len(p) and p[j] == '*':
            more = True
            j += 1
        if more:
            i_list = self.match_zero_or_more(s, c)
            for i in i_list:
                if self.__is_match(s[i:], p[j:]):
                    self.dp_add(s, p, True)
                    return True
            self.dp_add(s, p, False)
            return False
        else:
            if len(s) > 0 and (c == '.' or c == s[0]):
                r = self.__is_match(s[1:], p[j:])
                self.dp_add(s, p, r)
                return r
            else:
                self.dp_add(s, p, False)
                return False

    def match_zero_or_more(self, s, c):
        if c == '.':
            return [i for i in xrange(0, len(s) + 1)]
        else:
            result = [0]
            for i in xrange(0, len(s)):
                if s[i] == c:
                    result.append(i + 1)
                else:
                    break
            return result


if __name__ == '__main__':
    sol = Solution()
    print sol.isMatch('aa', 'a')
    print sol.isMatch('aa', 'aa')
    print sol.isMatch('aaa', 'aa')
    # print sol.match_zero_or_more('aa', 'a')
    print sol.isMatch('aa', 'a*')
    print sol.isMatch('aa', '.*')
    print sol.isMatch('ab', '.*')
    print sol.isMatch('aab', 'c*a*b')
    print sol.isMatch('ab', '.*c')
