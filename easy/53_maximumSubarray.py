# -*- coding:utf-8 -*-
#! /usr/bin/python3

import unittest
import sys

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

"""
    Divide and conquer
    AC
"""
class Solution2:
    def maxSubArray(self, nums):
        if nums == []:
            return None
        return self.divideAndConquer(nums, 0, len(nums))

    def divideAndConquer(self, nums, beg, end):
        if (end-beg == 1):
            return nums[beg]
        else:
            middle = int((end+beg)/2)
            leftMax = self.divideAndConquer(nums, beg, middle)
            rightMax = self.divideAndConquer(nums, middle, end)
            crossMax = self.getCrossInternalMax(nums, beg, middle, end)

            return max(leftMax, rightMax, crossMax)


    def getCrossInternalMax(self, nums, beg, middle, end):
        numsSum = 0
        leftNumsMax = nums[middle] 
        for i in range(middle, end):
            numsSum += nums[i]
            leftNumsMax = max(leftNumsMax, numsSum)

        numsSum = 0  
        rightNumsMax = nums[middle]
        for i in range(middle, beg-1, -1):
            numsSum += nums[i]
            rightNumsMax = max(rightNumsMax, numsSum)

        return rightNumsMax + leftNumsMax - nums[middle]


class Unittest_maxSubArray(unittest.TestCase):
    def setUp(self):
        # self.sol = Solution()
        self.sol = Solution2()

    def test_defaultSample(self):
        l = [-2,1,-3,4,-1,2,1,-5,4]
        expectedResult = 6
        self.assertEqual(expectedResult, self.sol.maxSubArray(l))

    def test_shortSample(self):
        l = [-2, 1, -3]
        expectedResult = 1
        ans = self.sol.maxSubArray(l)
        self.assertEqual(expectedResult, ans)

    def test_shortSample2(self):
        l = [4,-1,2,1]
        expectedResult = 6
        ans = self.sol.maxSubArray(l)
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

    def tearDown(self):
        self.sol = None

if __name__ == "__main__":
    unittest.main()
