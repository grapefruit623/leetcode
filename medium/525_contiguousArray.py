# -*- coding: utf-8 -*-
#! /usr/bin/python3
import unittest
from typing import List

class Solution:
    '''
        AC
        ref: leetcode's solution
    '''
    def findMaxLength(self, nums: List[int])->int:
        hashTable = dict()
        score = 0 
        ans = 0
        '''
            Why!!
        '''
        hashTable[0] = -1

        for i in range(len(nums)):
            score += 1 if nums[i] == 1 else -1 
            if score in hashTable:
                ans = max(ans, i-hashTable[score])
            else:
                hashTable[score] = i

        return ans

class Unittest_findMaxLength(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_sample1(self):
        inp = [0,1]
        expected = 2
        self.assertEqual(self.sol.findMaxLength(inp), expected)

    def test_sample2(self):
        inp = [0,1,0]
        expected = 2
        self.assertEqual(self.sol.findMaxLength(inp), expected)

    def test_sample3(self):
        inp = [0,1,0,1,1]
        expected = 4
        self.assertEqual(self.sol.findMaxLength(inp), expected)

    def test_sample4(self):
        inp = [1,1,0,0]
        expected = 4
        self.assertEqual(self.sol.findMaxLength(inp), expected)

    def test_sample5(self):
        inp = [1,0,1,0,1,0]
        expected = 6
        self.assertEqual(self.sol.findMaxLength(inp), expected)

    def test_sampleWA1(self):
        inp = [0,1,1,0,1,1,1,0]
        expected = 4
        self.assertEqual(self.sol.findMaxLength(inp), expected)

if __name__ == '__main__':
    unittest.main()
