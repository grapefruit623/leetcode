# -*- coding: utf-8 -*-
#! /usr/bin/python3

import unittest

class Solution:
    """
        AC
        But very slowly! Just faster than 8.73% python3 solutions!!!
        Need to improve performance, it close to O(n^2) time complexity.
    """
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        charLocTable = {}
        longest = 0
        startPos = 0
        endPos = len(s)
        currentLen = 0

        while startPos < endPos:
            currentChar = s[startPos]
            if currentChar not in charLocTable.keys():
                charLocTable[ currentChar ] = startPos
                currentLen += 1
                startPos += 1

                if currentLen > longest:
                    longest = currentLen
            else:
                startPos = charLocTable[ currentChar ]+1
                currentLen = 0
                charLocTable.clear()
        
        return longest

class Unittest_lengthOfLongestSubstring(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        data = "abcabcbb"
        expected = 3
        self.assertEqual(expected, self.sol.lengthOfLongestSubstring(data))

    def test_example2(self):
        data = "bbbbb"
        expected = 1
        self.assertEqual(expected, self.sol.lengthOfLongestSubstring(data))

    def test_example3(self):
        data = "pwwkew"
        expected = 3
        self.assertEqual(expected, self.sol.lengthOfLongestSubstring(data))

    def test_emptyStr(self):
        data = ""
        expected = 0
        self.assertEqual(expected, self.sol.lengthOfLongestSubstring(data))

    def test_oneChar(self):
        data = "a"
        expected = 1
        self.assertEqual(expected, self.sol.lengthOfLongestSubstring(data))

    def test_example_WA(self):
        data = "dvdf"
        expected = 3
        self.assertEqual(expected, self.sol.lengthOfLongestSubstring(data))

    def tearDown(self):
        self.sol = None

if __name__ == "__main__":
    unittest.main()
