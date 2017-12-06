# coding=utf-8

pair_map = {
    '(': ')',
    '{': '}',
    '[': ']',
}


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for c in s:
            if c in pair_map:
                stack.append(c)
            else:
                if len(stack) > 0 and pair_map[stack[-1]] == c:
                    stack.pop()
                else:
                    return False
        return len(stack) == 0


if __name__ == '__main__':
    sol = Solution()
    print sol.isValid('[]')
