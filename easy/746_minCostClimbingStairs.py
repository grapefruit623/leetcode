# -*- coding: utf-8 -*-
#! /usr/bin/python3
import unittest

"""
    AC
"""
class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        if len(cost) < 3:
            return max(cost)

        dpTable = []
        
        for i in range(len(cost)):
            if i < 2:
                dpTable.append( cost[i] )
            else:
                dpTable.append( min(cost[i]+dpTable[i-1], cost[i]+dpTable[i-2]) )

        return min(dpTable[-1], dpTable[-2])

class Unitest_minCoseClimbingStairs(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_shotExample(self):
        cost = [2, 3]
        expected = 3
        self.assertEqual(expected, self.sol.minCostClimingStaris(cost))

    def test_example1(self):
        cost = [10, 15, 20]
        expected = 15
        self.assertEqual(expected, self.sol.minCostClimingStaris(cost))

    def test_example2(self):
        cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
        expected = 6
        self.assertEqual(expected, self.sol.minCostClimingStaris(cost))

    def tearDown(self):
        self.sol = None

if __name__ == "__main__":
    unittest.main()
