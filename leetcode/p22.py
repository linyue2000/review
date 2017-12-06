# coding=utf-8

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.cache = {}
        return self.dfs(n, 0, 0)

    def dfs(self, n, opened, closed):
        if opened + closed == n * 2:
            return []
        if opened == n:
            return [')' * (n - closed)]
        if closed > opened:
            return []
        results = []
        next_results = self.dfs(n, opened + 1, closed)
        for next_result in next_results:
            results.append('(' + next_result)
        next_results = self.dfs(n, opened, closed + 1)
        for next_result in next_results:
            results.append(')' + next_result)
        return results


if __name__ == '__main__':
    s = Solution()
    print s.generateParenthesis(3)
