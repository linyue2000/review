# coding=utf-8
max = 0x7fffffff
min = -(max + 1)
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x > max or x < min:
            return 0
        if x == 0:
            return 0
        negative = False
        if x < 0:
            negative = True
            x = -x
        leading_zero = True
        r = 0
        while x > 0:
            digit = x % 10
            if digit > 0:
                leading_zero = False
            if not leading_zero:
                r = r * 10 + digit
            x /= 10
        if negative:
            r = -r
        if r > max or r < min:
            return 0
        return r


if __name__ == '__main__':
    sol = Solution()
    print sol.reverse(123)
    print sol.reverse(-321)
    print sol.reverse(120)
