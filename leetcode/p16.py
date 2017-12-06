# coding=utf-8
import math


class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        nums.sort()
        min_offset = None
        nearest = None
        for i in xrange(0, len(nums) - 2):
            if i == 0 or nums[i] != nums[i - 1]:
                l = i + 1
                r = len(nums) - 1
                while l < r:
                    test = nums[i] + nums[l] + nums[r]
                    if test == target:
                        return target
                    else:
                        offset = test - target
                        if min_offset is None or math.fabs(offset) < math.fabs(min_offset):
                            min_offset = offset
                            nearest = test
                        if test < target:
                            l += 1
                        else:
                            r -= 1
        return nearest


if __name__ == '__main__':
    sol = Solution()
    print sol.threeSumClosest([0, 1, 2], 3)
    print sol.threeSumClosest([1, 1, -1], 1)
    # print sol.threeSumClosest([-1, 2, 1, -4], 1)
    # print sol.threeSumClosest([0, 0, 0], 1)
    # print sol.threeSumClosest([0, 0, 0, 0, 0, 0], 1)
    # print sol.threeSumClosest([-4, -2, -2, -2, 0, 1, 2, 2, 2, 3, 3, 4, 4, 6, 6], 1)
