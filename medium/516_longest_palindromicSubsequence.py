# -*- coding:utf-8 -*-
#! /usr/bin/python3
import unittest

'''
    AC
    ref: https://www.cnblogs.com/grandyang/p/6493182.html

    Example

    bbbab

    dp is

    12334
     1223
      113
       11
        1
'''
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        l=len(s)
        
        if l == 1:
            return 1

        dp=[]

        for i in range(l):
            dp.append( [0]*l )


        for i in range(l-1, -1, -1):
            for j in range(i, l):
                if i == j:
                    dp[i][j] = 1;
                else:
                    if s[i] == s[j]:
                        dp[i][j] = dp[i+1][j-1]+2
                    else:
                        dp[i][j] = max(dp[i][j-1], dp[i+1][j])

        return dp[0][l-1]
        
class Unittest(unittest.TestCase):
    def setUp(self):
        self.sol=Solution()

    def test_case1(self):
        s="bbbab"
        expect=4

        self.assertEqual(expect, self.sol.longestPalindromeSubseq(s))

if __name__ == "__main__":
    unittest.main()
