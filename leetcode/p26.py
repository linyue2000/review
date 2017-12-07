#coding=utf-8

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_number = None
        i = 0
        for num in nums:
            if max_number is None or num > max_number:
                nums[i] = num
                max_number = num
                i += 1
        return i


