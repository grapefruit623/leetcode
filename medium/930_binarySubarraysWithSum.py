#! -*- coding: utf-8 -*-
import unittest
from typing import List

class Solution:
    '''
        WA
    '''
    def numSubarraysWithSum(self, A: List[int], S: int)->int:
        ans = 0
        dic = {0:1} # save count of prefix sum
        tempSum = 0

        for a in A:
            tempSum += a
            if tempSum-S in dic:
                ans += dic[tempSum-S] 

            if tempSum not in dic:
                dic[tempSum] = 1
            else:
                dic[tempSum] += 1

        return ans

class Unittest(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_sample1(self):
        inp = [1,0,1,0,1]
        s = 2
        expected = 4
        self.assertEqual(expected, self.sol.numSubarraysWithSum(inp, s))
        
    def test_sample_wa1(self):
        inp = [0,0,0,0,0]
        s = 0
        expected = 15 
        self.assertEqual(expected, self.sol.numSubarraysWithSum(inp, s))

    def test_sample_wa2(self):
        inp = [0,1,1,1,1]
        s = 3
        expected = 3 
        self.assertEqual(expected, self.sol.numSubarraysWithSum(inp, s))

if __name__ == "__main__":
    unittest.main()
