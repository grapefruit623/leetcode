# -*- coding: utf-8 -*-
#! /usr/bin/python3
import unittest

"""
    AC
"""
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        #Can not buy and sell in same day.
        if len(prices) < 2:
            return 0 

        startPos = 0
        endPos = 0
        profit = 0

        while endPos < len(prices):
            temp = prices[endPos]-prices[startPos]
            if temp < 0:
                startPos = endPos
            elif temp > profit:
                profit = temp
            
            endPos += 1

        return profit

class Unittest_maxProfit(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        data = [7,1,5,3,6,4]
        expected = 5
        self.assertEqual(expected, self.sol.maxProfit(data))

    def test_example2(self):
        data = [7,6,4,3,1]
        expected = 0
        self.assertEqual(expected, self.sol.maxProfit(data))

    def test_example_invalid1(self):
        data = [7]
        expected = 0
        self.assertEqual(expected, self.sol.maxProfit(data))

    def test_example_goodProfit(self):
        data = [1,5]
        expected = 4
        self.assertEqual(expected, self.sol.maxProfit(data))

    def test_example_increase(self):
        data = [1,5,7]
        expected = 6
        self.assertEqual(expected, self.sol.maxProfit(data))

    def test_example_haveDecrease(self):
        data = [7,5,8]
        expected = 3
        self.assertEqual(expected, self.sol.maxProfit(data))

    def test_example_haveDecrease2(self):
        data = [5,8,7]
        expected = 3
        self.assertEqual(expected, self.sol.maxProfit(data))


    def tearDown(self):
        self.sol = None

if __name__ == "__main__":
    unittest.main()
