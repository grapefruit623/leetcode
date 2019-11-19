# -*- coding: utf-8 -*-
#! /usr/bin/python
import unittest
from typing import List

class Solution:
    '''
        AC
        dp[i][j] means A[i]~B[j] have repeated subarray
        and records its length
    '''
    def findLength(self, A: List[int], B: List[int])->int:
        lenA = len(A)
        lenB = len(B)

        if lenA == 0 or lenB == 0:
            return 0

        dp = []
        for i in range(lenA+1):
            dp.append([0]*(lenB+1))

        ans = -1    

        for i in range(1,lenA+1):
            for j in range(1,lenB+1):
                if A[i-1] == B[j-1]:
                    dp[i][j] = max(dp[i-1][j-1]+1, 1)
                ans = max(ans, dp[i][j])
        return ans

class Unittest_findLength(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_sample1(self):
        a = [1,2,3,2,1]
        b = [3,2,1,4,7]
        expected = 3
        self.assertEqual(self.sol.findLength(a,b), expected)

    def test_sampleWA2(self):
        a = [0,1,1,1,1]
        b = [1,0,1,0,1]
        expected = 2
        self.assertEqual(self.sol.findLength(a,b), expected)

    def test_sample2(self):
        a = [1,2,5,3,2]
        b = [1,2,4,3,2]
        expected = 2
        self.assertEqual(self.sol.findLength(a,b), expected)

    def test_sampleWA3(self):
        a = [1,0,0,0,1]
        b = [1,0,0,1,1]
        expected = 3
        self.assertEqual(self.sol.findLength(a,b), expected)


if __name__ == '__main__':
    unittest.main()
