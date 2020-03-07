# -*- coding: utf-8 -*-
import unittest
from typing import List

class Solution:
    def maxProfit(self, prices: List[int])->int:
        n = len(prices)

        if n <= 1:
            return 0

        sell = [ 0 for i in range(n) ]
        cool = [ 0 for i in range(n) ]
        dp = [ 0 for i in range(n) ]

        for i in range(n):
            for j in range(i):
                if j-2 >= 0:
                    sellGain = max(prices[i]-prices[j] + cool[j-1],
                                    prices[i]-prices[j],
                                    prices[i]-prices[j] + dp[j-2])
                    sell[i] = max(sell[i], sellGain)
                else:
                    sell[i] = max(sell[i], prices[i]-prices[j])
                
                dp[i] = max(dp[j], sell[i], cool[i])
                cool[i] = max(cool[i], sell[i-1])

        print (cool)
        print (sell)
        print (dp)
        return max(dp)            

class Unittest_maxProfit(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_sample1(self):
        data = [1,2,3,0,2]
        expected = 3
        self.assertEqual(expected, self.sol.maxProfit(data))

    def test_sample2(self):
        data = [1,3,2,2,5]
        expected = 5
        self.assertEqual(expected, self.sol.maxProfit(data))

    def test_sample3(self):
        data = []
        expected = 0
        self.assertEqual(expected, self.sol.maxProfit(data))

    def test_sample4(self):
        data = [4,2,7,1,11]
        expected = 10
        self.assertEqual(expected, self.sol.maxProfit(data))

    def test_sample5(self):
        data = [6,1,6,4,3,0,2]
        expected = 7
        self.assertEqual(expected, self.sol.maxProfit(data))

    def test_sample6(self):
        data = [1,3,5,4,3,7,6,9,2,4]
        expected = 10
        self.assertEqual(expected, self.sol.maxProfit(data))

    def test_sample7(self):
        data = [0,8,5,7,4,7]
        expected = 11
        self.assertEqual(expected, self.sol.maxProfit(data))


if __name__ == '__main__':
    unittest.main()
