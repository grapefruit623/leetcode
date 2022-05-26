# -*- coding:utf-8 -*-
#! /usr/bin/python3
import unittest
from typing import List


class Solution:
    def integerBreak(self, n: int) -> int:
        dp=[-1]*(n+1)
        dp[1] = 1
        dp[2] = 1

        '''
            Renew dp[i] value step by step.
        '''
        for i in range(2, n+1):
            for j in range(1, i):
                dp[i] = max(dp[i], j*(i-j), dp[j]*(i-j), j*dp[i-j], dp[j]*dp[i-j])

        return dp[-1]

'''
    AC but slowly
'''
class Solution_recursive:
    def integerBreak(self, n: int) -> int:
        '''
            dp[i] is max product of number i.
        '''
        self.dp=[-1]*(n+1)
        self.dp[1] = 1
        self.dp[2] = 1
        return self.recursive(n)

    def recursive(self, n):
        if n == 0:
            return 0
        
        if n <= 2:
            return 1

        if self.dp[n] != -1:
            return self.dp[n]

        for i in range(1, n):
            l = self.recursive(i)
            r = self.recursive(n-i)

            self.dp[n] = max(self.dp[n], l*r ,
                                        i*r,
                                        l*(n-i),
                                        i*(n-i))

        return self.dp[n]

        
class Unittest(unittest.TestCase):
    def setUp(self):
        self.sol=Solution()

    def test_case1(self):
        n=2
        expect=1

        self.assertEqual(expect, self.sol.integerBreak(n))

    def test_case2(self):
        n=3
        expect=2

        self.assertEqual(expect, self.sol.integerBreak(n))

    def test_case3(self):
        n=10
        expect=36

        self.assertEqual(expect, self.sol.integerBreak(n))

if __name__ == "__main__":
    unittest.main()

