#! /usr/bin/python3
# -*- coding: utf-8 -*-
import unittest
from typing import List

class Solution:
    '''
        AC
    '''
    def findPairs(self, nums: List[int], k:int)->int:
        nums = sorted(nums)
        table = dict()
        ans = 0

        # absoulte difference must be not negative value
        if k < 0:
            return 0

        for n in nums:
            table[n] = table.setdefault(n, 0) + 1

        for n in table.keys():
            if n + k == n :
                if table[n] >= 2:
                    ans += 1
            elif n + k in table:
                ans += 1

        return ans

class Unittest_findPairs(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_sample1(self):
        inp = [3,1,4,1,5]
        k = 2
        self.assertEqual(2, self.sol.findPairs(inp, k))

    def test_sample2(self):
        inp = [1,2,3,4,5]
        k = 1
        self.assertEqual(4, self.sol.findPairs(inp, k))

    def test_sample3(self):
        inp = [1,3,1,5,4]
        k = 0
        self.assertEqual(1, self.sol.findPairs(inp, k))

    def test_sample5(self):
        inp = [1,2,3,4,5]
        k = -1
        self.assertEqual(0, self.sol.findPairs(inp, k))

if __name__ == "__main__":
    unittest.main()
