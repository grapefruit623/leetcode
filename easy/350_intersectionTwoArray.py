# -*- coding:utf-8 -*-
#! /usr/bin/python3
import unittest
from typing import List

class Solution:
    '''
        AC
    '''
    def intersect(self, nums1:List[int], nums2:List[int])->List[int]:
        if not nums1 or not nums2:
            return []

        nums1.sort()
        nums2.sort()
        nums1Len = len(nums1)
        nums2Len = len(nums2)
        n1Ptr = n2Ptr = 0
        ans = []

        while n1Ptr < nums1Len and n2Ptr < nums2Len:
            n1, n2 = nums1[n1Ptr], nums2[n2Ptr]
            if n1 == n2:
                ans.append(n1)
                n1Ptr += 1
                n2Ptr += 1
            else:
                if n1 > n2:
                    n2Ptr += 1
                elif n1 < n2:
                    n1Ptr += 1

        return ans

class Unittest_intersect(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_sample1(self):
        nums1 = [1,2,2,1]
        nums2 = [2,2]
        self.assertEqual([2,2], self.sol.intersect(nums1, nums2))

    def test_sample2(self):
        nums1 = [4,9,5]
        nums2 = [9,4,9,8,4]
        self.assertEqual([4,9], self.sol.intersect(nums1, nums2))

    def test_sample3(self):
        nums1 = [4,9,5]
        nums2 = []
        self.assertEqual([], self.sol.intersect(nums1, nums2))

if __name__ == "__main__":
    unittest.main()
