# -*- coding:utf-8 -*-
#! /usr/bin/python3
import unittest

class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        arr=[0,1]

        if n == 0:
            return 0

        if n<=1:
            return 1

        for i in range(2,n+1):
            temp=int(i/2)
            if i % 2==0:
                arr.append(arr[temp])
            else:
                arr.append(arr[temp]+arr[temp+1])

        print (arr)
        return max(arr)

class Unittest(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()
    
    def test_case1(self):
        n=7
        expect=3

        self.assertEqual(expect, self.sol.getMaximumGenerated(n))

    '''
        WA case
    '''
    def test_case2(self):
        n=15
        expect=5

        self.assertEqual(expect, self.sol.getMaximumGenerated(n))

if __name__ == "__main__":
    unittest.main()
