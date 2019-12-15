# -*- coding: utf-8 -*-
#! /usr/bin/python3
import unittest

class Solution:
    '''
        AC
    '''
    def longestCommonSubsequence(self, text1:str, text2:str) -> int:
        dp = []
        for i in range(len(text1)+1):
            dp.append( [0]*(len(text2)+1) )

        for row in range(1, len(text1)+1):
            for col in range(1, len(text2)+1):
                if text1[row-1] == text2[col-1]:
                    dp[row][col] = dp[row-1][col-1] + 1
                else:
                    dp[row][col] = max(dp[row-1][col], dp[row][col-1])
        
        return dp[-1][-1]

class Unittest_longestCommonSubsequence(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        t1 = 'abcde'
        t2 = 'ace'
        expected = 3
        self.assertEqual(self.sol.longestCommonSubsequence(t1, t2), expected)

    def test_case2(self):
        t1 = 'abc'
        t2 = 'abc'
        expected = 3
        self.assertEqual(self.sol.longestCommonSubsequence(t1, t2), expected)

    def test_case3(self):
        t1 = 'abc'
        t2 = 'df'
        expected = 0
        self.assertEqual(self.sol.longestCommonSubsequence(t1, t2), expected)

    def test_case4(self):
        t1 = 'aaa'
        t2 = ''
        expected = 0
        self.assertEqual(self.sol.longestCommonSubsequence(t1, t2), expected)

    def test_case5(self):
        t1 = 'ababc'
        t2 = 'aa'
        expected = 2
        self.assertEqual(self.sol.longestCommonSubsequence(t1, t2), expected)

if __name__ == '__main__':
    unittest.main()
