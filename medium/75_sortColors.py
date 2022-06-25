# -*- coding:utf-8 -*
#! /usr/bin/python3

import unittest
from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        loc_0 = 0
        loc_2 = len(nums)-1
        i = loc_0
        
        while loc_0 < loc_2 and i <= loc_2:
            if nums[i] == 1:
                i += 1
            elif nums[i] == 2:
                nums[i], nums[loc_2] = nums[loc_2], nums[i]
                loc_2 -= 1
            elif nums[i] == 0:
                nums[i], nums[loc_0] = nums[loc_0], nums[i]
                loc_0 += 1
                i += 1

class Unittest(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        nums = [2,0,2,1,1,0]
        expected = [0,0,1,1,2,2]

        self.sol.sortColors(nums)
        self.assertEqual(expected, nums)

    def test_case2(self):
        nums = [2,0,1]
        expected = [0,1,2]

        self.sol.sortColors(nums)
        self.assertEqual(expected, nums)

if __name__ == '__main__':
    unittest.main()
