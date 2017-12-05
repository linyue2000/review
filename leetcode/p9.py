# coding=utf-8

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        temp = x
        y = 0
        while temp > 0:
            y = y * 10 + temp % 10
            temp /= 10
        return x == y


if __name__ == '__main__':
    sol = Solution()
    print sol.isPalindrome(1)
