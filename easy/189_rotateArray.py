# -*- coding:utf-8 -*-
#! /usr/bin/python3
import unittest

class Solution:
    """
        AC
    """
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead
        """
        l = len(nums)
        k = k%l
        nums2N = nums + nums
        nums2NRotate = nums2N[l-k:2*l-k]
        for i in range(l):
            nums[i] = nums2NRotate[i]

class Unittest_rotate(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()
    
    def test_sample1(self):
        data = [1,2,3,4,5,6,7]
        k = 3
        expected = [5,6,7,1,2,3,4]
        self.sol.rotate(data, k)
        self.assertEqual(expected, data)

    def test_sample2(self):
        data = [1,2]
        k = 5
        expected = [2,1]
        self.sol.rotate(data, k)
        self.assertEqual(expected, data)

    def test_wa1(self):
        data = [-1]
        k = 2
        expected = [-1]
        self.sol.rotate(data, k)
        self.assertEqual(expected, data)

if __name__ == "__main__":
    unittest.main()
