# -*- coding:utf-8 -*-
#! /usr/bin/python3
import unittest
from typing import List

class Solution:
    def findLengthOfLCIS(self, nums:List)->int:
        i = j = 0
        ans = 0

        while j < len(nums):
            if i == j:
                j += 1
            else:
                if nums[j] > nums[j-1]:
                    j += 1
                else:
                    i = j
            ans = max(ans, j-i)

        return ans

class Unittest_findLengthOfLCIS(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_sample1(self):
        data = [1,3,5,4,7]
        expected = 3
        self.assertEqual(expected, self.sol.findLengthOfLCIS(data))

    def test_sample2(self):
        data = [2,2,2,2,2]
        expected = 1
        self.assertEqual(expected, self.sol.findLengthOfLCIS(data))

    def test_sample3(self):
        data = []
        expected = 0
        self.assertEqual(expected, self.sol.findLengthOfLCIS(data))

if __name__ == '__main__':
    unittest.main()
