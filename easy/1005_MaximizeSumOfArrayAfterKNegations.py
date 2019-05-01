# -*- coding:utf-8 -*-
#! /usr/bin/python3
import unittest
from typing import List

'''
    leetcode tag: Greedy
'''
class Solution:
    '''
        AC
    '''
    def largestSumAfterKNegations(self, A:List[int], K:int)->int:
        a = sorted(A)
        i = 0
        
        '''
            Inverse negivation numbers.
        '''
        while K > 0:
            if a[i] < 0:
                a[i] *= -1
                K -= 1
            else:
                break
            i += 1

        '''
            Eventhough there are still negative number,
            but the smallers are inversed to positive.
        '''
        if K == 0:
            return sum(a)

        '''
            All remaining negation used on zero,
            all negative number are inversed to positive.
        '''
        a = sorted(a)
        if a[0] == 0:
            return sum(a)

        '''
            All numbers are positive now, we need to chose smaller to be
            negation.
            Because sign of number will not be modified by twice nagivation.
            Just care about K mod 2 and inversed the smallest number.
        '''
        K %= 2
        a[0] *= -1 if K == 1 else 1

        return sum(a)



class Unittest(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_sample1(self):
        A = [4,2,3]
        K = 1
        expected = 5
        self.assertEqual(expected, self.sol.largestSumAfterKNegations(A,K))

    def test_sample2(self):
        A = [3,-1,0,2]
        K = 3
        expected = 6
        self.assertEqual(expected, self.sol.largestSumAfterKNegations(A,K))

    def test_sample3(self):
        A = [2,-3,-1,5,-4]
        K = 2
        expected = 13
        self.assertEqual(expected, self.sol.largestSumAfterKNegations(A,K))

    def test_sample4(self):
        A = [-2,9,9,8,4]
        K = 5 
        expected = 32 
        self.assertEqual(expected, self.sol.largestSumAfterKNegations(A,K))

if __name__ == "__main__":
    unittest.main()
