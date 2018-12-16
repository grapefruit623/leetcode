# -*- coding:utf-8 -*-
#! /usr/bin/python3

import unittest

class Solution(object):
    def __init__(self):
        self.pascalTriangle = []
    """
        AC
    """
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows < len(self.pascalTriangle):
            return self.pascalTriangle[:numRows]

        for row in range(len(self.pascalTriangle), numRows):
            if row == 0:
                self.pascalTriangle.append( [1] )
            else:
                prevRow = self.pascalTriangle[row-1]
                currRow = [1]
                for i in range(len(prevRow)):
                    if i+1 < len(prevRow):
                        currRow.append(prevRow[i]+prevRow[i+1])
                    else:
                        currRow.append(1)
                self.pascalTriangle.append(currRow)            

        return self.pascalTriangle

class Unittest_generate(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_sample(self):
        rows = 2
        expected = [ [1], [1,1]]
        self.assertEqual(expected, self.sol.generate(rows))

    def test_sample1(self):
        rows = 5
        expected = [ [1], [1,1], [1,2,1], [1,3,3,1], [1,4,6,4,1] ]
        self.assertEqual(expected, self.sol.generate(rows))

    def test_emptySample(self):
        rows = 0
        expected = []
        self.assertEqual(expected, self.sol.generate(rows))

if __name__ == "__main__":
    unittest.main()
