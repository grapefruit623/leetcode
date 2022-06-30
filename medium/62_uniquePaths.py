# -*-coding:utf-8 -*-
#! /usr/bin/python3
import unittest

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [ [0 for j in range(n)] for i in range(m) ]

        for col in range(n):
            dp[0][col] = 1

        for row in range(m):
            dp[row][0] = 1

        for row in range(1, m):
            for col in range(1, n):
                dp[row][col] = dp[row-1][col] + dp[row][col-1]

        return dp[m-1][n-1]

class Unittest(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        m = 3
        n = 7
        expect = 28
        self.assertEqual(expect, self.sol.uniquePaths(m, n))

if __name__ == "__main__":
    unittest.main()
