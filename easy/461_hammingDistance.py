# -*- coding:utf-8 -*-
#! /usr/bin/python3
import unittest

"""
    AC but slowly...
"""
class Solution():
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        xorResult = x ^ y
        bitStr = bin(xorResult)[2:]

        return bitStr.count('1')

class Unittest_hammingDistance(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_default(self):
        x = 1
        y = 4
        expAns = 2
        self.assertEqual(expAns, self.sol.hammingDistance(x, y))

    def test_zero(self):
        x = 0
        y = 0
        expAns = 0
        self.assertEqual(expAns, self.sol.hammingDistance(x, y))

    def test_oneAndThree(self):
        x = 1
        y = 3
        expAns = 1
        self.assertEqual(expAns, self.sol.hammingDistance(x, y))

    def test_longestDistance(self):
        x = 0
        y = 2**31-1
        expAns = 31
        self.assertEqual(expAns, self.sol.hammingDistance(x, y))

    def tearDown(self):
        self.sol = None

if __name__ == '__main__':
    unittest.main()
