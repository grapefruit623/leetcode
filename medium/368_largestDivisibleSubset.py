# -*- coding: utf-8 -*-
#! /usr/bin/python3
import unittest
from typing import List

class Solution:
    '''
        ref: https://www.geeksforgeeks.org/largest-divisible-subset-array/
    '''
    def largestDivisibleSubset(self, nums: List[int])->List[int]:

        if len(nums) == 0:
            return []

        nums = sorted(nums)
        tempAns = []
        ans = []

        # dp[i] store size of divisible subset
        dp = [1]*(len(nums))

        # prevElements store previous element's index before
        # nums[i] 
        prevElementIndexs = [-1]*(len(nums))

        # curent maximum number in divisible subset
        currentMaxIndex = 0 

        for i in range(len(nums)):
            for j in range(i):
                # If current element nums[j] can make more longer divisible subset after nums[i].
                # Record the previous element which can get the longest divisible subset before nums[i].
                if nums[i] % nums[j] == 0 and dp[i] < dp[j] + 1:
                    # Size of subset contained nums[i] is size of subset contained element[j] + 1  
                    dp[i] = dp[j] + 1
                    prevElementIndexs[i] = j

            # Remember who is the last element.
            if dp[i] > dp[currentMaxIndex]:
                currentMaxIndex = i

        # Traverse all stored element index to create ans.
        k = currentMaxIndex 
        while k >= 0:
            ans.append(nums[k])
            k = prevElementIndexs[k]

        ans.reverse()
        return ans

class Unittest_largestDivisibleSubset(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()
    
    def test_sample1(self):
        inp = [1,2,3]
        expected = [1,2]
        self.assertEqual(expected, self.sol.largestDivisibleSubset(inp))

    def test_sample2(self):
        inp = [1,2,4,8]
        expected = [1,2,4,8]
        self.assertEqual(expected, self.sol.largestDivisibleSubset(inp))

    def test_sample3(self):
        inp = [2,3,8,9,10,27]
        expected = [3,9,27]
        self.assertEqual(expected, self.sol.largestDivisibleSubset(inp))

    def test_sample4(self):
        inp = []
        expected = []
        self.assertEqual(expected, self.sol.largestDivisibleSubset(inp))

    def test_sampleWA1(self):
        inp = [1,3,9,18,54,90,108,180,360,540,720]
        # WA [1,3,9,18,54,108,540]
        expected = [1,3,9,18,90,180,360,720]
        self.assertEqual(expected, self.sol.largestDivisibleSubset(inp))

    def test_sampleWA2(self):
        inp = [4,8,10,240]
        # WA [1,3,9,18,54,108,540]
        expected = [4,8,240]
        self.assertEqual(expected, self.sol.largestDivisibleSubset(inp))

if __name__ == '__main__':
    unittest.main()
