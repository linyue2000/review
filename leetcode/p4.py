# coding=utf-8

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        size1 = len(nums1)
        size2 = len(nums2)
        total = size1 + size2
        if total % 2 == 1:
            odds = False
            median_index = total / 2
        else:
            odds = True
            median_index = total / 2 - 1
        i, j = 0, 0
        for k in xrange(0, median_index + 1):
            # 为了运行效率就不封装成函数调用了
            if i == size1:
                num = nums2[j - 1]
                j += 1
            elif j == size2:
                num = nums1[i]
                i += 1
            else:
                n1 = nums1[i]
                n2 = nums2[j]
                if n1 < n2:
                    num = n1
                    i += 1
                else:
                    num = n2
                    j += 1
        if not odds:
            return float(num)
        else:
            # 为了运行效率就不封装成函数调用了
            if i == size1:
                num_ = nums2[j]
                j += 1
            elif j == size2:
                num_ = nums1[i]
                i += 1
            else:
                n1 = nums1[i]
                n2 = nums2[j]
                if n1 < n2:
                    num_ = n1
                    i += 1
                else:
                    num_ = n2
                    j += 1
            return (float(num) + float(num_)) / 2


if __name__ == '__main__':
    sol = Solution()
    print sol.findMedianSortedArrays([1, 3], [2])
    print sol.findMedianSortedArrays([1, 2], [3, 4])
