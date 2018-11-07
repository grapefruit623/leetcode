# -*- coding: utf-8 -*-
#! /usr/bin/python3

import unittest

"""
    AC
"""
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        bit1Count = 0

        while n != 0:
            if n % 2 != 0:
                bit1Count += 1

            n >>= 1 

        return bit1Count

class Unittest_hammingWeight(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        d = 11
        expected = 3
        self.assertEqual(expected, self.sol.hammingWeight(d))

    def test_example2(self):
        d = 128
        expected = 1
        self.assertEqual(expected, self.sol.hammingWeight(d))

    def tearDown(self):
        self.sol = None

if __name__ == "__main__":
    unittest.main()
