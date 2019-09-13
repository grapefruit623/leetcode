# -*- coding: utf-8 -*-
import unittest
from typing import List

class Solution:
    '''
        AC
    '''
    def stoneGame(self, piles: List[int])->bool:
        self.piles = piles
        self.dp = {}
        scoreDiff = self.miniMax(0, len(self.piles)-1, 1)

        print ('scoreDiff: ', scoreDiff)
        if scoreDiff > 0:
            return True
        else:
            return False

    def miniMax(self, i, j, isAlexTurn=1):
        if i == j:
            return self.piles[i]*isAlexTurn
        else:
            leftDp = 0
            rightDp = 0
            if (i+1,j,-1*isAlexTurn) not in self.dp.keys(): 
                self.dp[ (i+1, j, -1*isAlexTurn) ] = self.miniMax(i+1,j, -1*isAlexTurn)

            left = isAlexTurn * self.piles[i] + self.dp[(i+1, j, -1*isAlexTurn)] 

            if (i, j-1, -1*isAlexTurn) not in self.dp.keys():
                self.dp[(i, j-1, -1*isAlexTurn)] = self.miniMax(i, j-1, -1*isAlexTurn)

            right = isAlexTurn * self.piles[j] + self.dp[(i, j-1, -1*isAlexTurn)] 

            if isAlexTurn == 1:
                return max(left, right)
            else:
                return min(left,right)

class Unittest_maxProfit(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_sample1(self):
        data = [5,3,4,5]
        expected = True
        self.assertEqual(expected, self.sol.stoneGame(data))

if __name__ == '__main__':
    unittest.main()
