# -*- coding: utf-8 -*-
#! /usr/bin/python3

import unittest

class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        return s[-1::-1]

class Unittest_reverseString(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        inputData = "hello"
        outputData = "olleh"
        self.assertEqual(outputData, self.sol.reverseString(inputData))

    def test_example2(self):
        inputData = "A man, a plan, a canal: Panama"
        outputData = "amanaP :lanac a ,nalp a ,nam A"
        self.assertEqual(outputData, self.sol.reverseString(inputData))

    def tearDown(self):
        self.sol = None

if __name__ == '__main__':
    unittest.main()

