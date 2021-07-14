# -*- coding:utf-8 -*-
#! /usr/bin/python3
import unittest
from typing import List

class Solution:
    def lengthOfLastWord(self, s: str)->int:
        arr = s.strip().split(' ')
        return len(arr[-1])

class Unittest(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_sample1(self):
        inp = "Hello World"
        expected = 5 
        self.assertEqual(expected, self.sol.lengthOfLastWord(inp))

    def test_sample2(self):
        inp = " "
        expected = 0 
        self.assertEqual(expected, self.sol.lengthOfLastWord(inp))

    def test_sample3(self):
        inp = "Hi append space "
        expected = 5 
        self.assertEqual(expected, self.sol.lengthOfLastWord(inp))


if __name__ == "__main__":
    unittest.main()
