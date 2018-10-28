# -*- coding:utf-8 -*-
#! /usr/bin/python3

import unittest

"""
    AC
"""
class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == []:
            return None

        self.dpTable = [0]*len(nums)
        self.dpTable[0] = max(float('-inf'), nums[0])

        for i in range(1, len(nums)):
            self.dpTable[i] = max(nums[i], self.dpTable[i-1]+nums[i])

        return max(self.dpTable)
        
class Unittest_maxSubArray(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_defaultSample(self):
        l = [-2,1,-3,4,-1,2,1,-5,4]
        expectedResult = 6
        self.assertEqual(expectedResult, self.sol.maxSubArray(l))

    def test_shortSample(self):
        l = [-2, 1, -3]
        expectedResult = 1
        ans = self.sol.maxSubArray(l)
        self.assertEqual( [-2,1,-2], self.sol.dpTable )
        self.assertEqual(expectedResult, ans)

    def test_shortSample2(self):
        l = [4,-1,2,1]
        expectedResult = 6
        ans = self.sol.maxSubArray(l)
        self.assertEqual( [4,3,5,6], self.sol.dpTable )
        self.assertEqual(expectedResult, ans)

    def test_emptyData(self):
        l = []
        expectedResult = None
        self.assertEqual(expectedResult, self.sol.maxSubArray(l))

    def test_onlyOneData(self):
        l = [-1]
        expectedResult = -1 
        self.assertEqual(expectedResult, self.sol.maxSubArray(l))

    def test_twoNegivateData(self):
        l = [-2,-1]
        expectedResult = -1
        ans = self.sol.maxSubArray(l)
        self.assertEqual(expectedResult, ans)

    def test_twoPositiveData(self):
        l = [1,2]
        expectedResult = 3
        ans = self.sol.maxSubArray(l)
        self.assertEqual(expectedResult, ans)
        self.assertEqual([1,3], self.sol.dpTable)

    def tearDown(self):
        self.sol = None

if __name__ == "__main__":
    unittest.main()
