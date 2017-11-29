# coding=utf-8

'''
s[i, j] = nums[i] + nums[j]

s11 s12 s13 s14 s15 
    s22 s23 s24 s25
        s33 s34 s35
            s44 s45
                s55

情况1，若s[l,r]>target，则排除第r列中，[l,r]下面所有元素（都>target），第r列中，[l,r]上面的元素已经都被情况2排除过了，所以可以r--
情况2，若s[l,r]<target，则排除第l行中，[l,r]左面所有元素（都<target），第l行中，[l,r]右面的元素已经都被情况1排除过了，所以可以l++

'''


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # 2分搜第一个r
        r = len(nums) - 1
        if r < 1:
            return None
        l = 1
        n = target - nums[0]
        r = self.bs(nums, l, r, n)
        if nums[r] < n and r < len(nums) - 1:
            r += 1
        #2分搜第一个l
        n = target - nums[r]
        l = self.bs(nums, 0, r - 1, n)
        if nums[l] > n and l > 0:
            l -= 1
        # 搜sum
        while l < r:
            s = nums[l] + nums[r]
            if s == target:
                return [l + 1, r + 1]
            elif s < target:
                l += 1
            else:
                r -= 1

    def bs(self, nums, l, r, n):
        m = 0
        while l <= r:
            m = l + (r - l) / 2
            if nums[m] == n:
                return m
            elif nums[m] > n:
                r = m - 1
            else:
                l = m + 1
        return m


if __name__ == '__main__':
    s = Solution()
    print s.twoSum([2, 7, 11, 15], 9)
