# -*- coding: utf-8 -*-
#! /usr/bin/python3
import unittest

class Solution(object):
    def __init__(self):
        self.ansCount = 0

    '''
        TLE
    '''
    def findTargetSumWays_TLE(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype int
        """

        if (len(nums) == 1):
            if nums[0] == S or -1*nums[0] == S:
                return 1

        self.dp = []
        self.ansCount = 0
        for i in range(len(nums)):
            self.dp.append([])
        self.dp[0].append(nums[0])
        self.dp[0].append(-1*nums[0])

        for startInd in range(1, len(nums)):
            for dpResult in self.dp[startInd-1]:
                self.dp[startInd].append( -1*nums[startInd] + dpResult )
                self.dp[startInd].append( nums[startInd] + dpResult )

        for d in self.dp[len(nums)-1]:
            if d == S:
                self.ansCount += 1

        return self.ansCount

    """
        AC
        Cost 1 second to deal all test case in leetcode website.
    """
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype int
        """
        self.hashTable = {}
        return self.recursiveCompare(nums, 0, 0, S)

    def recursiveCompare(self, nums, index, s, target):
        if index == len(nums):
            if s == target:
                return 1
            else:
                return 0
        
        key = str([index, s])
        if key in self.hashTable.keys():
            return self.hashTable[key]
        else:
            count = self.recursiveCompare(nums, index+1, s+nums[index], target) \
                    + self.recursiveCompare(nums, index+1, s-nums[index], target)
            self.hashTable[key] = count
            return count

class Unittest_findTargetSumWays(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_sample1(self):
        nums = [1,1,1,1,1]
        s = 3 
        expected = 5
        self.assertEqual(expected, self.sol.findTargetSumWays(nums, s))

    def test_sample2(self):
        nums = [1]
        s = 1 
        expected = 1
        self.assertEqual(expected, self.sol.findTargetSumWays(nums, s))

    def test_sample3(self):
        nums = [29,6,7,36,30,28,35,48,20,44,40,2,31,25,6,41,33,4,35,38]
        s = 35 
        expected = 0
        self.assertEqual(expected, self.sol.findTargetSumWays_TLE(nums, s))

    def test_sample4(self):
        nums = [42,24,30,14,38,27,12,29,43,42,5,18,0,1,12,44,45,50,21,47]
        s = 38
        expected = 5602
        self.assertEqual(expected, self.sol.findTargetSumWays(nums, s))

    def test_sample5(self):
        nums = [2,107,109,113,127,131,137,3,2,3,5,7,11,13,17,19,23,29,47,53]
        s = 2
        expected = 2790
        self.assertEqual(expected, self.sol.findTargetSumWays(nums, s))

if __name__ == '__main__':
    unittest.main()
    
