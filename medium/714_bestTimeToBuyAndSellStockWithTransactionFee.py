# -*- coding: utf-8 -*-
import unittest
from typing import List

class Solution:

    '''
        The dp state transcation is based on leetcode 309.
    '''
    def maxProfit(self, prices: List[int], fee:int)->int:
        n = len(prices)
        if n <= 1:
            return 0
        sell = [ 0 for i in range(n) ]
        buy = [0 for i in range(n) ]

        buy[0] = -prices[0]

        for i in range(1, n):
            sell[i] = max(sell[i-1], buy[i-1]+prices[i]-fee)
            buy[i] = max(buy[i-1], sell[i-1]-prices[i])

        return sell[n-1]

class Unittest_maxProfit(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_sample1(self):
        data = [1,3,2,8,4,9]
        fee = 2
        expected = 8
        self.assertEqual(expected, self.sol.maxProfit(data,fee))

if __name__ == '__main__':
    unittest.main()
