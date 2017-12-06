# coding=utf-8

m = {
    '1': '?',
    '2': 'abc',
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrs',
    '8': 'tuv',
    '9': 'wxyz',
    '0': ' ',
}


class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        return self.combination(digits, 0)

    def combination(self, digits, start):
        number = digits[start]
        letters = m[number]
        if start == len(digits) - 1:
            result = [c for c in letters]
        else:
            next_results = self.combination(digits, start + 1)
            result = []
            for c in letters:
                result.extend([c + next_result for next_result in next_results])
        return result


if __name__ == '__main__':
    sol = Solution()
    print sol.letterCombinations('23')
