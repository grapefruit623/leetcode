# -*-coding: utf-8 -*-
#! /usr/bin/python3
import unittest
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        start=0
        l=len(prices)
        ans=0

        for end in range(0, l):
            tempProfit=prices[end]-prices[start]

            if tempProfit > 0:
                ans += tempProfit
                start=end
            else:
                start=end

        return ans

class Unittest(unittest.TestCase):
    def setUp(self):
        self.sol=Solution()

    def test_case1(self):
        prices=[7,1,5,3,6,4]
        expect = 7
        self.assertEqual(expect, self.sol.maxProfit(prices))

if __name__ == "__main__":
    unittest.main()
