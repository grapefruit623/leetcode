# -*- coding:utf-8 -*-
import unittest

'''
    ref:
        http://bangbingsyb.blogspot.com/2014/11/leetcode-unique-binary-search-trees-i-ii.html
'''
class Solution:
    '''
        AC

        dp[i] means counts of bsts in i nodes.
        dp[0] means empty tree, it only one combination
        dp[1] mans only root node, it only one combination

        dp[2] = dp[0]*dp[1] + dp[1]*dp[0]
                (root=1)       (root=2)

                   (1)                   (2)
              (Nil)    (2)            (1)  (Nil)

        dp[3] = dp[0]*dp[2]    # (root=1, left=nil, right=2,3)
                + dp[1]*dp[1]  # (root=2, left=1, right=3)
                + dp[2]*dp[0]  # (root=3, left=1,2, right=nil)
    '''
    def numTrees(self, n:int)->int:
        dp = [1,1]

        for i in range(2, n+1):
            temp = 0
            for j in range(0,i):
                temp += dp[j]*dp[i-1-j]
            dp.append(temp)

        return dp[n]

class Unittest_numTrees(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_sample1(self):
        inp = 3
        expected = 5
        self.assertEqual(expected, self.sol.numTrees(inp))

    def test_sample2(self):
        inp = 4
        expected = 14 
        self.assertEqual(expected, self.sol.numTrees(inp))

if __name__ == "__main__":
    unittest.main()
