# coding=utf-8

class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        results = []
        for i in xrange(0, len(nums) - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in xrange(i + 1, len(nums) - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                left = j + 1
                right = len(nums) - 1
                while left < right:
                    test = nums[i] + nums[j] + nums[left] + nums[right]
                    if test == target:
                        results.append([nums[i], nums[j], nums[left], nums[right]])
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                    if test <= target:
                        left += 1
                    else:
                        right -= 1
        return results


if __name__ == '__main__':
    sol = Solution()
    print sol.fourSum([3, 1, -9, -9, 9, -4, -2, 5, 10, 6, 8, -7, -8, -7, 8, 2, 9, -1], -20)
    print sol.fourSum([1, 0, -1, 0, -2, 2], 0)
    # print sol.fourSum([-5, -2, -1, 0, 2, 2, 4, 4, 4], 12)
    # print sol.nSum([-5,-2,-1, 0, 2, 2, 4, 4, 4], 12, 4, 0)
    # print sol.nSum([2, -1, 0, 0, 1, 2], 0, 4, 0)
