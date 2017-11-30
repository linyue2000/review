# coding=utf-8

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        vb = 2 * numRows - 2
        nb = len(s) / vb
        result = ''
        for r in xrange(0, numRows):
            b_vb = 0
            for b in xrange(0, nb + 1):
                i1 = b_vb + r
                if i1 < len(s):
                    result += s[i1]
                else:
                    break
                r_ = vb - r
                if r_ < vb and r_ != r:
                    i2 = b_vb + r_
                    if i2 < len(s):
                        result += s[i2]
                    else:
                        break
                b_vb += vb
        return result


if __name__ == '__main__':
    sol = Solution()
    print sol.convert('PAYPALISHIRING', 1)
    print sol.convert('PAYPALISHIRING', 3)
