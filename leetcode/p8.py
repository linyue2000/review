# coding=utf-8
max = 0x7fffffff
min = -(max + 1)

STATUS_PRE = 0
STATUS_FLAG = 1
STATUS_SEQUENCING = 2
STATUS_FINISH = 3
STATUS_ILLEGAL = 4


class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        status = STATUS_PRE
        r = 0
        flag = 1
        digit_read = 0
        for c in str:
            #
            if status == STATUS_PRE:
                if c != ' ':
                    status = STATUS_FLAG
            #
            if status == STATUS_FLAG:
                status = STATUS_SEQUENCING
                if c == '-':
                    flag = -1
                    continue
                if c == '+':
                    continue
            #
            if status == STATUS_SEQUENCING:
                if ord(c) < ord('0') or ord(c) > ord('9'):
                    status = STATUS_ILLEGAL if digit_read == 0 else STATUS_FINISH
                else:
                    digit_read += 1
                    r = r * 10 + int(c)
                    if flag * r < min:
                        return min
                    if flag * r > max:
                        return max
            #
            if status == STATUS_FINISH:
                return flag * r
            #
            if status == STATUS_ILLEGAL:
                return 0
        return flag * r


if __name__ == '__main__':
    sol = Solution()
    print sol.myAtoi("123")
    print sol.myAtoi("-321")
    print sol.myAtoi("120")
    print sol.myAtoi("123 123")
    print sol.myAtoi("- 321")
    print sol.myAtoi("    -120")
    print sol.myAtoi("    120")
    print sol.myAtoi("    66sedkgj")
    print sol.myAtoi("    -zdkgj")
    print sol.myAtoi("-2147483648")
