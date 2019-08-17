# -*- coding: utf-8 -*-
#! /usr/bin/python3
import unittest
from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int])->int:
        l = len(nums)
        if l == 0:
            return 0

        dp = [0]*l
        dp[0] = 1 # length 1 of single char
        maxValuePtr = 0

        for i in range(1, l):
            temp = 0
            if nums[i] > nums[i-1]:
                temp = dp[i-1] + 1
            else:
                temp = 1

            if i-2 >= 0:
                if nums[i] > nums[i-2]:
                    temp = max(temp, dp[i-2]+1)

            if nums[i] > nums[maxValuePtr]:
                if dp[maxValuePtr]+1 >= temp:
                    temp = dp[maxValuePtr] + 1
                    maxValuePtr = i

            dp[i] = temp 

        return max(dp)


class Unittest_lengthOfLIS(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_sample1(self):
        data = [10,9,2,5,3,7,101,18]
        expected = 4
        self.assertEqual(expected, self.sol.lengthOfLIS(data))

    def test_sample2(self):
        data = [10]
        expected = 1
        self.assertEqual(expected, self.sol.lengthOfLIS(data))

    def test_sample3(self):
        data = [10,9]
        expected = 1
        self.assertEqual(expected, self.sol.lengthOfLIS(data))

    def test_sample4(self):
        data = [1,9]
        expected = 2
        self.assertEqual(expected, self.sol.lengthOfLIS(data))

    def test_sample5(self):
        data = []
        expected = 0
        self.assertEqual(expected, self.sol.lengthOfLIS(data))

    def test_sample6(self):
        data = [1,2,3]
        expected = 3
        self.assertEqual(expected, self.sol.lengthOfLIS(data))

    def test_sample7(self):
        data = [1,3,2,3]
        expected = 3
        self.assertEqual(expected, self.sol.lengthOfLIS(data))

    def test_sample8(self):
        data = [8,3,2,3]
        expected = 2
        self.assertEqual(expected, self.sol.lengthOfLIS(data))

    def test_sample9(self):
        data = [8,3,4,9]
        expected = 3
        self.assertEqual(expected, self.sol.lengthOfLIS(data))

    def test_sample10(self):
        data = [2,2]
        expected = 1
        self.assertEqual(expected, self.sol.lengthOfLIS(data))

    def test_sample11(self):
        data = [11,12,13,14,15,6,7,8,101,18]
        expected = 6
        self.assertEqual(expected, self.sol.lengthOfLIS(data))

if __name__ == '__main__':
    unittest.main()
