# -*- coding: utf-8 -*-
#! /usr/bin/python3
import unittest
from typing import List

class NumArray:
    '''
        AC
    '''
    def __init__(self, nums: List[int]):
        self.dp = [0]*(len(nums)+1)
        for i in range(0,len(nums)):
            self.dp[i+1] = self.dp[i] + nums[i]

    def sumRange(self, i: int, j: int)->int:
        return self.dp[j+1] - self.dp[i]

class Unittest_NumArray(unittest.TestCase):
    def setUp(self):
        pass

    def test_case1(self):
        self.numArray = NumArray([-2,0,3,-5,2,-1])
        self.assertEqual(self.numArray.sumRange(0,2), 1)
        self.assertEqual(self.numArray.sumRange(2,5), -1)
        self.assertEqual(self.numArray.sumRange(0,5), -3)

if __name__ == "__main__":
    unittest.main()
