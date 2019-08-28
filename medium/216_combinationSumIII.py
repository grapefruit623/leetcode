# -*- coding: utf-8 -*-
#! /usr/bin/python
import unittest
from typing import List

class Solution:
    def combinationSum3(self, k: int, n: int)->List[List[int]]:
        self.ans = []
        self.recursive(0, k, n, [], [ i for i in range(1, 10) ])
        return self.ans

    '''
        AC
        Backtracking
    '''
    def recursive(self, index, k, n, currentAns, nums):
        if k == 0:
            if sum(currentAns) == n:
                self.ans.append( [ a for a in currentAns ] )
            return

        for i in range(index, len(nums)):
            currentAns.append( nums[i] )
            self.recursive(i+1, k-1, n, currentAns, nums)
            currentAns.pop()

class Unittest_combinationSum3(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_sample1(self):
        k = 3
        n = 7
        expected = [ [1,2,4] ]
        self.assertEqual(expected, self.sol.combinationSum3(k, n))

    def test_sample2(self):
        k = 3
        n = 9
        expected = [ [1,2,6], [1,3,5], [2,3,4] ]
        self.assertEqual(expected, self.sol.combinationSum3(k, n))

    def test_sample3(self):
        k = 5
        n = 15 
        expected = [ [1,2,3,4,5] ]
        self.assertEqual(expected, self.sol.combinationSum3(k, n))

if __name__ == '__main__':
    unittest.main()
