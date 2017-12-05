# coding=utf-8

digit_map={
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000,
}


class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        i = 0
        while i < len(s):
            c1 = s[i]
            n1 = digit_map[c1]
            if i + 1 < len(s):
                c2 = s[i + 1]
                n2 = digit_map[c2]
                if n2 > n1:
                    n = n2 - n1
                    i += 1
                else:
                    n = n1
            else:
                n = n1
            i += 1
            result += n
        return result



if __name__ == '__main__':
    sol = Solution()
    print sol.romanToInt("C")
