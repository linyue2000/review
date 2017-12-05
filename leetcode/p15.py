# coding=utf-8

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        results = []
        for i in xrange(0, len(nums) - 2):
            if i == 0 or nums[i] != nums[i - 1]:
                result2s = self.twoSum(nums, i + 1, -nums[i])
                for result2 in result2s:
                    result2[0:0] = [nums[i]]
                    results.append(result2)
        return results

    def twoSum(self, nums, start_index, sum):
        results = []
        l = start_index
        r = len(nums) - 1
        while l < r:
            test = nums[l] + nums[r]
            if test == sum:
                results.append([nums[l], nums[r]])
                while l < r and nums[l] == nums[l + 1]:
                    l += 1
                while l < r and nums[r] == nums[r - 1]:
                    r -= 1
                l += 1
                r -= 1
            elif test < sum:
                l += 1
            else:
                r -= 1
        return results


if __name__ == '__main__':
    sol = Solution()
    print sol.threeSum([-1, 0, 1, 0])
    print sol.threeSum([0, 0, 0, 0, 0, 0])
    print sol.threeSum([-4, -2, -2, -2, 0, 1, 2, 2, 2, 3, 3, 4, 4, 6, 6])
