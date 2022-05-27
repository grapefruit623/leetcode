# -*- coding:utf-8 -*-
#! /usr/bin/python3
import unittest
from typing import List

class Solution:
    def getRow(self, rowIndex: int)->List[int]:
        pascalTriangle=[]
        
        for i in range(rowIndex+1):
            pascalTriangle.append([0]*(rowIndex+1))

        for i in range(rowIndex+1):
            pascalTriangle[i][0] = 1

        for i in range(rowIndex+1):
            pascalTriangle[0][i] = 1

        for i in range(1, rowIndex):
            for j in range(1, rowIndex-i+1):
                pascalTriangle[i][j] = pascalTriangle[i-1][j]+pascalTriangle[i][j-1]
            
        ans=[]

        for i in range(rowIndex, -1, -1):
            ans.append(pascalTriangle[i][rowIndex-i])

        return ans

class Unittest(unittest.TestCase):
    def setUp(self):
        self.sol=Solution()

    def test_case1(self):
        rowIndex=3
        expect=[1,3,3,1]

        self.assertEqual(expect, self.sol.getRow(rowIndex))

if __name__ == "__main__":
    unittest.main()
