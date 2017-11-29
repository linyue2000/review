#coding=utf-8

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        m = {}
        i = 0
        for a in nums:
            b = target - a
            if b in m:
                i1 = m[b]
                return [i1, i]
            m[a] = i
            i += 1
        return None


if __name__ == '__main__':
    s = Solution()
    print s.twoSum([2, 7, 11, 15], 9)
