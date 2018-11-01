# -*- coding: utf-8 -*-
#! /usr/bin/python3

import unittest

class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        sPos = 0
        numsLen = len(nums)

        while sPos < numsLen:
            if nums[sPos] == 0:
                v = nums.pop(sPos)
                nums.append(v)
                numsLen -= 1
            else:
                sPos += 1

class Unittest_moveZeroes(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        data = [0,1,0,3,12]
        expected = [1,3,12,0,0]
        self.sol.moveZeros(data)
        self.assertEqual(expected, data)

    def test_example2(self):
        data = [1,3,12,0,0]
        expected = [1,3,12,0,0]
        self.sol.moveZeros(data)
        self.assertEqual(expected, data)

    def test_example3(self):
        data = [1,3,12]
        expected = [1,3,12]
        self.sol.moveZeros(data)
        self.assertEqual(expected, data)

    def test_empty(self):
        data = []
        expected = []
        self.sol.moveZeros(data)
        self.assertEqual(expected, data)

    def tearDown(self):
        self.sol = None
if __name__ == "__main__":
    unittest.main()
