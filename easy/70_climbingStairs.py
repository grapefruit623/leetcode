# -*- coding: utf-8 -*-
#! /usr/bin/python3
import unittest

"""
    AC
"""
class Solution(object):
    def __init__(self):
        self.fibonacci = [1,1]

    """
        fibonacci formula solution
    """
    def climbStairsV2(self, n):
        import math
        fn = ( 1/math.sqrt(5) )*( math.pow( ( (1+math.sqrt(5))/2 ), n+1 ) - 
                                    math.pow( ( (1-math.sqrt(5))/2 ), n+1) )
        return int(fn)

    """
        Dynamic programing solution
    """
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        dpTableLen = len(self.fibonacci)
        while dpTableLen <= n:
            self.fibonacci.append( self.fibonacci[dpTableLen-2] + self.fibonacci[dpTableLen-1] )
            dpTableLen += 1

        return self.fibonacci[n]
             

class Unittest_climbStairs(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        data = 2
        expected = 2
        self.assertEqual(expected, self.sol.climbStairs(data))

    def test_example2(self):
        data = 3
        expected = 3
        self.assertEqual(expected, self.sol.climbStairs(data))

    def test_multiple(self):
        data = 2
        expected = 2
        self.assertEqual(expected, self.sol.climbStairs(data))

        data = 3
        expected = 3
        self.assertEqual(expected, self.sol.climbStairs(data))

    def test_example1_v2(self):
        data = 2
        expected = 2
        self.assertEqual(expected, self.sol.climbStairsV2(data))

    def test_example2_v2(self):
        data = 3
        expected = 3
        self.assertEqual(expected, self.sol.climbStairsV2(data))

    def tearDown(self):
        self.sol = None

if __name__ == "__main__":
    unittest.main()

