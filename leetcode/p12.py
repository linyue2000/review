# coding=utf-8

dimens = [1000, 500, 100, 50, 10, 5, 1]
digits = {}
digits[1] = 'I'  # can be a decreasor
digits[5] = 'V'
digits[10] = 'X'  # can be a decreasor
digits[50] = 'L'
digits[100] = 'C'  # can be a decreasor
digits[500] = 'D'
digits[1000] = 'M'


class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        if 0 == num:
            return ''
        if 0 < num <= 3:
            return digits[1] * num
        elif num < 5:
            return digits[1] + digits[5]
        elif num < 9:
            return self.get_num_add(num, 5)
        elif num < 10:
            return self.get_num_dec(num, 10, 1)
        elif num < 40:
            return self.get_num_add(num, 10)
        elif num < 50:
            return self.get_num_dec(num, 50, 10)
        elif num < 90:
            return self.get_num_add(num, 50)
        elif num < 100:
            return self.get_num_dec(num, 100, 10)
        elif num < 400:
            return self.get_num_add(num, 100)
        elif num < 500:
            return self.get_num_dec(num, 500, 100)
        elif num < 900:
            return self.get_num_add(num, 500)
        elif num < 1000:
            return self.get_num_dec(num, 1000, 100)
        elif num < 4000:
            return self.get_num_add(num, 1000)

    def get_num_add(self, num, dimen):
        quotient = num / dimen
        remainder = num % dimen
        return digits[dimen] * quotient + self.intToRoman(remainder)

    def get_num_dec(self, num, dimen1, dimen2):
        return digits[dimen2] + digits[dimen1] + self.intToRoman(num - (dimen1 - dimen2))


if __name__ == '__main__':
    sol = Solution()
    print sol.intToRoman(86)
    print sol.intToRoman(87)
    print sol.intToRoman(88)
    print sol.intToRoman(89)
    print sol.intToRoman(90)
    print sol.intToRoman(95)
    print sol.intToRoman(96)
    print sol.intToRoman(98)
    print sol.intToRoman(99)
