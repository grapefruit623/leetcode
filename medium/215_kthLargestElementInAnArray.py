# -*- coding: utf-8 -*-
#! /usr/bin/python3
import unittest

class Solution(object):
    """
        AC
    """
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        return None if nums == [] else sorted(nums)[-k:][0]

class Unittest_findKthLargest(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_sample1(self):
        data = [3,2,1,5,6,4]
        k = 2
        expected = 5
        self.assertEqual(expected, self.sol.findKthLargest(data, k))

    def test_sample2(self):
        data = [3,2,3,1,2,4,5,5,6]
        k = 4
        expected = 4
        self.assertEqual(expected, self.sol.findKthLargest(data, k))

    def test_sample3(self):
        data = [1]
        k = 1
        expected = 1
        self.assertEqual(expected, self.sol.findKthLargest(data, k))

    def test_emptySample(self):
        data = []
        k = 0
        expected = None
        self.assertEqual(expected, self.sol.findKthLargest(data, k))

if __name__ == "__main__":
    unittest.main()
