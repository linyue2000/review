# coding=utf-8

class Solution(object):
    def maxArea(self, x):
        """
        :type height: List[int]
        :rtype: int
        """
        l, r = 0, len(x) - 1
        low = min(x[l], x[r])
        m = (r - l) * low
        while l < r:
            if x[l] == low:
                while l < r and x[l] <= low:
                    l += 1
            else:
                while l < r and x[r] <= low:
                    r -= 1
            low = min(x[l], x[r])
            m = max(m, (r - l) * low)
        return m



if __name__ == '__main__':
    sol = Solution()
    print sol.maxArea([1, 2])
