# -*- coding:utf-8 -*-
import unittest
from typing import List

class Solution:
    '''
        Dynamic programing
    '''
    def minPathSum(self, grid:List[List[int]])->int:
        row = len(grid)
        col = len(grid[0])

        '''
            Only one dimension array
            i.e. [ [1,2,3] ]
            i.e. [ [1],[2],[3] ]
        '''
        if row == 1:
            return sum(grid[0])

        if col == 1:
            return sum(rows[0] for rows in grid)

        '''
            initial dp table
        '''
        dp = []
        for i in range(row):
            dp.append([0]*col)

        dp[0][0] = grid[0][0]

        '''
            initial first row and first col's dp solution
        '''
        for j in range(1, col):
            dp[0][j] = dp[0][j-1]+grid[0][j]
        for i in range(1, row):
            dp[i][0] = dp[i-1][0]+grid[i][0]
        
        for i in range(1, row):
            for j in range(1, col):
                dp[i][j] = min(dp[i-1][j]+grid[i][j],
                               dp[i][j-1]+grid[i][j])
        return dp[-1][-1]

class unittest_minPathSum(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_sample1(self):
        data = [ [1,3,1],
                 [1,5,1],
                 [4,2,1]
               ]
        expected = 7
        self.assertEqual(expected, self.sol.minPathSum(data))

    def test_sample2(self):
        data = [ [1,3,1],
               ]
        expected = 5
        self.assertEqual(expected, self.sol.minPathSum(data))

    def test_sample3(self):
        data = [ [1],
                 [3],
                 [7],
                 [4],
               ]
        expected = 15
        self.assertEqual(expected, self.sol.minPathSum(data))

    def test_sample4(self):
        data = [ [1],
               ]
        expected = 1
        self.assertEqual(expected, self.sol.minPathSum(data))

    def test_sample4(self):
        data = [ [],
               ]
        expected = 0 
        self.assertEqual(expected, self.sol.minPathSum(data))

if __name__ == "__main__":
    unittest.main()
