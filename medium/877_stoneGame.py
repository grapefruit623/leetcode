# -*- coding: utf-8 -*-
import unittest
from typing import List

class Solution:
    def stoneGame(self, piles: List[int])->bool:
        return self.dynamicProgram_stoneGame(piles)

    '''
        Dynamic programing
        AC
        Ref: Solution.
    '''
    def dynamicProgram_stoneGame(self, piles):
        dp = []
        for i in range(len(piles)):
            dp.append([0]*len(piles))
            dp[i][i] = piles[i]
        
        for i in range(len(piles)-1, -1, -1):
            for j in range(i, len(piles)):
                if i == j:
                    continue
                else:
                    if (j-i+1) % 2 == 1: # first player
                        dp[i][j] = max(piles[j] + dp[i][j-1], piles[i] + dp[i+1][j])
                    else:
                        dp[i][j] = max(-piles[j] + dp[i][j-1], -piles[i] + dp[i+1][j])

        return True if dp[0][len(piles)-1] > 0 else False

    '''
        AC
        But slowly
    '''
    def recursive_stoneGame(self, piles):
        self.piles = piles
        self.dp = {}
        self.miniMax(0, len(self.piles)-1)
        return True if self.dp[(0, len(self.piles)-1)] > 0 else False

    def miniMax(self, i, j, isAlexTurn=1):
        if (i,j) in self.dp.keys():
            return
        if i == j:
            self.dp[(i,j)] = self.piles[i]*isAlexTurn
        else:
            leftDp = 0
            rightDp = 0

            if (i+1,j) not in self.dp.keys(): 
                self.miniMax(i+1,j, -1*isAlexTurn)
            left = isAlexTurn * self.piles[i] + self.dp[(i+1, j)] 

            if (i,j-1) not in self.dp.keys():
                self.miniMax(i, j-1, -1*isAlexTurn)
            right = isAlexTurn * self.piles[j] + self.dp[(i, j-1)] 

            if isAlexTurn == 1:
                self.dp[ (i,j) ] = max(left, right)
            else:
                self.dp[ (i,j) ] = min(left,right)

class Unittest_maxProfit(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_sample1(self):
        data = [5,3,4,5]
        expected = True
        self.assertEqual(expected, self.sol.stoneGame(data))

if __name__ == '__main__':
    unittest.main()
