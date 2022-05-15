# -*- coding:utf-8 -*-
#! /usr/bin/python3
import unittest

class Solution:
    def fib(self, n: int)->int:
        fibArr=[0,1]

        if n < 2:
            return fibArr[n]

        for i in range(2, n+1):
            fibArr.append(fibArr[i-2]+fibArr[i-1])

        return fibArr[n]

class Unittest(unittest.TestCase):
    def setUp(self):
        self.sol=Solution()

    def test_case1(self):
        n=4
        expected=3
        self.assertEqual(expected, self.sol.fib(n))

if __name__ == "__main__":
    unittest.main()
