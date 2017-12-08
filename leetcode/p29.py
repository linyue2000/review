# coding=utf-8

MAX_INT = 0x7fffffff
MIN_INT = -0x80000000

import math


class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if divisor == 0:
            return MAX_INT
        flag = 1 if dividend >= 0 and divisor >= 0 or dividend <= 0 and divisor <= 0 else -1
        dividend = int(math.fabs(dividend))
        divisor = int(math.fabs(divisor))
        quotient = 0
        q_add = 1
        num_dec = divisor
        while dividend >= num_dec or (q_add > 0 and dividend >= divisor):
            if dividend >= num_dec:
                dividend -= num_dec
                quotient += q_add
                q_add <<= 1
                num_dec <<= 1
            else:
                q_add >>= 1
                num_dec >>= 1
        quotient = quotient * flag
        if quotient > MAX_INT:
            return MAX_INT
        if quotient < MIN_INT:
            return MAX_INT
        return quotient


if __name__ == '__main__':
    s = Solution()
    print  s.divide(999999999, 2)
