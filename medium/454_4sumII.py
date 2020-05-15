# -*- coding:utf-8 -*-
#! /usr/bin/python3
import unittest
from typing import List
from typing import Dict

class Solution:
    '''
        AC
    '''
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int])->int:
        if len(A) == 0:
            return 0

        ans = 0
        hashTable1 = self.getTwoSumHashTable(A,B)
        hashTable2 = self.getTwoSumHashTable(C,D)

        for h1 in hashTable1:
            if -h1 in hashTable2:
                ans += hashTable1[h1]*hashTable2[-h1]
        
        return ans

    def getTwoSumHashTable(self, A: List[int], B: List[int]) -> Dict:
        hashTable = dict()

        for i in A:
            for j in B:
               hashTable.setdefault(i+j, 0)
               hashTable[i+j] += 1

        return hashTable

class Unittest_fourSumCount(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_sample1(self):
        A = [1,2]
        B = [-2,-1]
        C = [-1,2]
        D = [0,2]
        expected = 2
        self.assertEqual(self.sol.fourSumCount(A,B,C,D), expected)

    def test_sample2(self):
        A = []
        B = []
        C = []
        D = []
        expected = 0
        self.assertEqual(self.sol.fourSumCount(A,B,C,D), expected)

if __name__ == '__main__':
    unittest.main()
