# -*- coding: utf-8 -*-
#! /usr/bin/python3
import unittest

class Solution:
    """
        No linear algebra solution.
        AC
    """
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        dimension = len(matrix)
        for row in range( int(dimension/2) ):
            for col in range(dimension):
                temp = matrix[row][col]
                matrix[row][col] = matrix[dimension-row-1][col]
                matrix[dimension-row-1][col] = temp

        for row in range(dimension):
            for col in range(row, dimension):
                temp = matrix[row][col]
                matrix[row][col] = matrix[col][row]
                matrix[col][row] = temp

class testRotateMatrix(unittest.TestCase):

    def setUp(self):
        self.sol = Solution()
    
    def test_case1(self):
        matrix = [ [1,2,3], [4,5,6], [7,8,9] ]
        result = [ [7,4,1], [8,5,2], [9,6,3] ]
        self.sol.rotate(matrix)
        self.assertEqual(matrix, result)

    def test_case2(self):
        matrix = [ [5,1,9,11], [2,4,8,10], [13,3,6,7], [15,14,12,16] ]
        result = [ [15,13,2,5], [14,3,4,1], [12,6,8,9], [16,7,10,11] ]
        self.sol.rotate(matrix)
        self.assertEqual(matrix, result)

    def test_case3(self):
        matrix = [ [1,1], [2,2] ]
        result = [ [1,1], [2,2] ]
        self.sol.rotate(matrix)
        self.assertNotEqual(matrix, result)

if __name__ == "__main__":
    trueSuite = unittest.TestSuite()
    trueSuite.addTest(testRotateMatrix('test_case1'))
    trueSuite.addTest(testRotateMatrix('test_case2'))

    falseSuite = unittest.TestSuite()
    falseSuite.addTest(testRotateMatrix('test_case3'))

    runner = unittest.TextTestRunner()
    runner.run(trueSuite)
    runner.run(falseSuite)
