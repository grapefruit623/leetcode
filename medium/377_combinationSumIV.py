# -*- coding:utf-8 -*-
#! /usr/bin/python3
from typing import List
import unittest

class Solution:
    '''
        AC
        This problem is similar to 377_coinChange and 70_climbingStairs

        dp[i] is combination ways to reach i
        dp[i+n] += dp[i] means that there is dp[i] ways to reach i+n by add n from i
    '''
    def combinationSum4(self, nums: List[int], target: int)->int:
        dp = [0]*(target+1)
        dp[0] = 1 
        for i in range(0, target):
            for n in nums:
                if i+n <= target:
                    dp[i+n] += dp[i]
        return dp[target]

    '''
        TLE
    '''
    def combinationSum4_tle(self, nums: List[int], target: int)->int:

        def recursive(nums, target, currentNums):
            for n in nums:
                s = sum(currentNums)
                if s > target:
                    return

                if s == target:
                    self.ans += 1
                    return

                currentNums.append(n)
                recursive(nums, target, currentNums)
                currentNums.pop()

        self.ans = 0
        nums = sorted(nums)
        recursive(nums, target, [])
        return self.ans


class Unittest_combinationSum4(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()
    
    def test_sample1(self):
        inp = [1,2,3]
        target = 4
        expected = 7
        self.assertEqual(expected, self.sol.combinationSum4(inp, target))

    def test_sample_tle(self):
        inp = [4,2,1]
        target = 32
        expected = 39882198
        self.assertEqual(expected, self.sol.combinationSum4(inp, target))

if __name__ == "__main__":
    unittest.main()

