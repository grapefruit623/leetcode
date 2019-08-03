# -*- coding:utf-8 -*-
import unittest
from typing import List

class Solution:
    '''
        AC
        Using recursion and memorization.
        Concept of solution comes from Approach #1 Using Recursion [Accepted]

    '''
    def PredictTheWinner(self, nums:List[int])->bool:
        dp = {}
        p1Score = self.calculateScore(nums, 0, len(nums)-1, 1, dp)
        print ('p1Score - p2Score: ', p1Score)
        return True if p1Score >= 0 else False


    def calculateScore(self, nums, i, j, turn, dp):
        if (i,j) in dp.keys():
            return dp[(i,j)]

        if i == j:
            dp[(i,j)] = turn * nums[i]
        else:
            l = turn * nums[i] + self.calculateScore(nums, i+1, j, -1*turn, dp)
            r = turn * nums[j] + self.calculateScore(nums, i, j-1, -1*turn, dp) 

            if turn == 1:
                dp[(i,j)] = max(l,r)
            else:
                dp[(i,j)] = min(l,r)

        return dp[(i,j)]

class Unittest_predictTheWinnder(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_sample1(self):
        data = [1,5,2]
        expected = False
        self.assertEqual(expected, self.sol.PredictTheWinner(data))

    def test_sample2(self):
        data = [1,5,233,7]
        expected = True
        self.assertEqual(expected, self.sol.PredictTheWinner(data))

    def test_sample3(self):
        data = [1,5,7]
        expected = True
        self.assertEqual(expected, self.sol.PredictTheWinner(data))

    def test_sample4(self):
        data = [504,427,95,397,468,485,326,112,296,290,106,148,12,334,23,296,122,187,141,187]
        expected = True
        self.assertEqual(expected, self.sol.PredictTheWinner(data))


if __name__ == '__main__':
    unittest.main()
