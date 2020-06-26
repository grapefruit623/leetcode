#! -*- coding: utf-8 -*-
import unittest
from typing import List

class Solution:
    '''
        AC
    '''
    def longestArithSeqLength(self, A: List[int]) -> int:
        '''
            Store all length by difference at each elements
        '''
        dic = dict()
        ans = 0
        dic[0] = dict()
        for i in range(len(A)):
            currDic = dict()
            for j in range(i):
                diff = A[i]-A[j]
                prevDic = dic.get(j)
                '''
                    prevDic.get(diff,1) is length cat be retrieved at element j with diff
                    +1 which means arithmetic sequence is increasing
                '''
                currentMax = prevDic.get(diff,1) + 1  
                currDic[diff] = currentMax
                ans = max(ans, currentMax)

            dic[i] = currDic

        return ans
                

class Unittest_longestArithSeqLength(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()
    
    def test_sample1(self):
        inp = [9,4,7,2,10]
        expected = 3    
        self.assertEqual(expected, self.sol.longestArithSeqLength(inp))

    def test_sample2(self):
        inp = [20,1,15,3,10,5,8]
        expected = 4
        self.assertEqual(expected, self.sol.longestArithSeqLength(inp))

    def test_sample_wa1(self):
        inp = [83,20,17,43,52,78,68,45]
        expected = 2
        self.assertEqual(expected, self.sol.longestArithSeqLength(inp))

    def test_sample_wa2(self):
        inp = [17,43,52,78]
        expected = 2
        self.assertEqual(expected, self.sol.longestArithSeqLength(inp))

if __name__ == '__main__':
    unittest.main()
