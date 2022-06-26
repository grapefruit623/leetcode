# -*-coding: utf-8 -*-
#! /usr/bin/python3

import unittest
from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        currentSubset = []
        
        self.helper(nums, 0, currentSubset, ans)
        
        return ans
        
    def helper(self, nums, index, currentSubset, ans):
        if currentSubset not in ans:
            ans.append(currentSubset[:])
                        
        for i in range(index, len(nums)):
            currentSubset.append(nums[i])
            self.helper(nums, i+1, currentSubset, ans)
            currentSubset.pop(-1)
        

class Unittest(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_sample1(self):
        nums = [1,2,3]
        expect = [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
        ret = self.sol.subsets(nums)

        for r in ret:
            self.assertIn(r, expect)

    def test_sample2(self):
        nums = [0]
        expect = [[],[0]]
        self.assertEqual(expect, self.sol.subsets(nums))

if __name__ == '__main__':
    unittest.main()
