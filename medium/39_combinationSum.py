# -*- coding: utf-8 -*-
#! /usr/bin/python
import unittest
from typing import List

class Solution:
    def combinationSum(self, candidates:List[int], target:int)->List[List[int]]:
        self.ans = []
        newCand = []
        candidates = sorted(candidates)
        self.recursive(candidates, 0, [], target)
        return self.ans

    '''
        AC
    '''
    def recursive(self, candidates, index, currentAns, currentSum):
        if index > len(candidates):
            return

        if currentSum == 0:
            if currentAns not in self.ans:
                self.ans.append( [ c for c in currentAns ])
            return
        else:
            for i in range(index, len(candidates)):
                if currentSum - candidates[i] >= 0:
                    currentAns.append(candidates[i])
                    self.recursive(candidates, i, currentAns, currentSum-candidates[i])
                    currentAns.pop()
                else:
                    '''
                        Because candidates was sorted, remaining element can not be
                        used in correct answer. 
                    '''
                    break


class Unittest_combinationSum(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_sample1(self):
        data = [2,3,6,7]
        target = 7
        expected = [ [2,2,3], [7] ] 
        self.assertEqual(expected, self.sol.combinationSum(data, target))

    def test_sample2(self):
        data = [2,3,5]
        target = 8
        expected = [ [2,2,2,2], [2,3,3], [3,5] ] 
        self.assertEqual(expected, self.sol.combinationSum(data, target))
        
    def test_sample3(self):
        data = []
        target = 0
        expected = [[]] 
        self.assertEqual(expected, self.sol.combinationSum(data, target))

    def test_sample4(self):
        data = []
        target = 3
        expected = [] 
        self.assertEqual(expected, self.sol.combinationSum(data, target))

    def test_sample5(self):
        data = [2,3,5]
        target = 7
        expected = [[2,2,3], [2,5]] 
        self.assertEqual(expected, self.sol.combinationSum(data, target))

    def test_sample6(self):
        data = [8,7,4,3]
        target = 11
        expected = [[3,4,4],[3,8],[4,7]]
        self.assertEqual(expected, self.sol.combinationSum(data, target))

if __name__ == "__main__":
    unittest.main()
