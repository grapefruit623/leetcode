# -*- coding:utf-8 -*-
#! /usr/bin/python3
import unittest

class Solution:
    def tribonacci(self, n: int)->int:
        tArr=[0,1,1]

        if n <= 2:
            return tArr[n]

        for i in range(3, n+1):
            tArr.append(tArr[i-3]+tArr[i-2]+tArr[i-1])

        return tArr[n]

class Unittest(unittest.TestCase):
    def setUp(self):
        self.sol=Solution()

    def test_case1(self):
        n=4
        expect=4
        self.assertEqual(expect, self.sol.tribonacci(n))

    def test_case2(self):
        n=25
        expect=1389537
        self.assertEqual(expect, self.sol.tribonacci(n))

if __name__ == "__main__":
    unittest.main()
