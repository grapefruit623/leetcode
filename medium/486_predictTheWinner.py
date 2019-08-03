# -*- coding:utf-8 -*-
import unittest
from typing import List

class Solution:
    '''
        TLE
        reference: Solution comes from Approach #1 Using Recursion [Accepted]
    '''
    def PredictTheWinner(self, nums:List[int])->bool:
        print (nums)
        p1Score = self.calculateScore(nums, 0, len(nums)-1, 1)
        print ('p1Score - p2Score: ', p1Score)
        return True if p1Score >= 0 else False


    def calculateScore(self, nums, i, j, turn):
        if i == j:
            return turn * nums[i]
        else:
            l = self.calculateScore(nums, i+1, j, -1*turn)
            l = turn * nums[i] + l 
            r = self.calculateScore(nums, i, j-1, -1*turn)
            r = turn * nums[j] + r 

            if turn == 1:
                return max(l, r)
            else:
                return min(l,r)


class Unittest_predictTheWinnder(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    '''
    def test_sample1(self):
        data = [1,5,2]
        expected = False
        self.assertEqual(expected, self.sol.PredictTheWinner(data))
    '''

    '''
    def test_sample2(self):
        data = [1,5,233,7]
        expected = True
        self.assertEqual(expected, self.sol.PredictTheWinner(data))
    '''
    def test_sample3(self):
        data = [1,5,7]
        expected = True
        self.assertEqual(expected, self.sol.PredictTheWinner(data))

if __name__ == '__main__':
    unittest.main()
