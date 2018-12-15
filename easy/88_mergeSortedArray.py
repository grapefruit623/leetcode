# -*- coding:utf-8 -*-
#! /usr/bin/python3
import unittest

class Solution(object):
    """
        AC very slowly.
    """
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :typen n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        totalLen = m+n
        nums2Index = 0

        while m < totalLen:
            nums1Index = m
            nums1[nums1Index] = nums2[nums2Index]
            while nums1Index > 0 and nums1[nums1Index-1] > nums1[nums1Index]:
                self.swap(nums1, nums1Index-1, nums1Index)
                nums1Index -= 1

            m += 1
            nums2Index += 1

    def swap(self, nums1, i, j):
        t = nums1[i]
        nums1[i] = nums1[j]
        nums1[j] = t

class Unittest_merge(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_sample1(self):
        nums1 = [1,2,3,0,0,0]
        m = 3
        nums2 = [2,5,6]
        n = 3
        expected = [1,2,2,3,5,6]
        self.sol.merge(nums1, m, nums2, n)
        self.assertEqual(expected, nums1)
    
    def test_empty(self):
        nums1 = [1,2,3,0,0,0]
        m = 3
        nums2 = []
        n = 0
        expected = [1,2,3,0,0,0]
        self.sol.merge(nums1, m, nums2, n)
        self.assertEqual(expected, nums1)

if __name__ == "__main__":
    unittest.main()
