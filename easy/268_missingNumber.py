# -*- coding:utf-8 -*-
#! /usr/bin/python3
import unittest
from typing import List

class Solution:
    '''
        AC
    '''
    def missingNumber(self, num: List[int])->int:
        num = sorted(num)
        l = len(num)

        i = l-1
        while i >= 0:
            if num[i] != l:
                return l
            i -= 1
            l -= 1

        return l 

class Unittest_missingNumber(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_sample1(self):
        inp = [3,0,1]
        self.assertEqual(2, self.sol.missingNumber(inp))

    def test_sample2(self):
        inp = [9,6,4,2,3,5,7,0,1]
        self.assertEqual(8, self.sol.missingNumber(inp))

    def test_sample3(self):
        inp = [0]
        self.assertEqual(1, self.sol.missingNumber(inp))

    def test_sample4(self):
        inp = [0,2]
        self.assertEqual(1, self.sol.missingNumber(inp))

    def test_sample5(self):
        inp = [1]
        self.assertEqual(0, self.sol.missingNumber(inp))

if __name__ == '__main__':
    unittest.main()
