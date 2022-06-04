# -*- coding:utf-8 -*-
#! /usr/bin/python3
import unittest
from typing import List

class Solution:
    '''
        AC
    '''
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp=[]

        for t in triangle:
            dp.append([0]*len(t))

        dp[0][0] = triangle[0][0]

        for i in range(1, len(triangle)):
            for j in range(0, i+1):
                if i == j:
                    dp[i][j] = dp[i-1][j-1] + triangle[i][j]
                else:
                    if j-1<0:
                        dp[i][j] = dp[i-1][j]+triangle[i][j]
                    else:
                        dp[i][j] = min(dp[i-1][j-1]+triangle[i][j], dp[i-1][j]+triangle[i][j])

        
        return min(dp[-1])


class Unittest(unittest.TestCase):
    def setUp(self):
        self.sol=Solution()

    def test_sample1(self):
        triangle=[[2], [3,4], [6,5,7], [4,1,8,3]]
        expect=11
        self.assertEqual(expect, self.sol.minimumTotal(triangle))
        
    def test_sample2(self):
        triangle=[[-10]]
        expect=-10
        self.assertEqual(expect, self.sol.minimumTotal(triangle))

if __name__ == "__main__":
    unittest.main()
