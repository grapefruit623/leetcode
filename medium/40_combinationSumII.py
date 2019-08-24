# -*- coding: utf-8 -*-
#! /usr/bin/python
import unittest
from typing import List

class Solution:
    def combinationSum2(self, candidates:List[int], target:int)->List[List[int]]:
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
                    self.recursive(candidates, i+1, currentAns, currentSum-candidates[i])
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
        data = [10,1,2,7,6,1,5]
        target = 8
        expected = [ [1,1,6], [1,2,5], [1,7], [2,6] ] 
        self.assertEqual(expected, self.sol.combinationSum2(data, target))

    def test_sample2(self):
        data = [2,5,2,1,2]
        target = 5
        expected = [ [1,2,2], [5] ] 
        self.assertEqual(expected, self.sol.combinationSum2(data, target))

if __name__ == "__main__":
    unittest.main()
