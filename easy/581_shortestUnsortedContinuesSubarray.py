# -*- coding: utf-8 -*-
#! /usr/bin/python3
import unittest

class Solution:
    """
        Solution by sorting
        time complexity is depend on Python's sorting algorithm.
        TLE
    """
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sortedNums = sorted(nums)
        ans = len(nums)
        count = 0
        for i in range(0, len(nums)):
            if sortedNums[i] == nums[i]:
                count += 1
            else:
                break

        if count == ans:
            return 0

        for i in range(len(nums)-1, -1, -1):
            if sortedNums[i] == nums[i]:
                count += 1
            else:
                break

        ans -= count
        return ans 

class Unittest_findUnsortedSubarray(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_sample1(self):
        data = [2,6,4,8,10,9,15]
        expected = 5
        self.assertEqual(expected, self.sol.findUnsortedSubarray(data))

    def test_sample2(self):
        data = [1,2,3,4]
        expected = 0
        self.assertEqual(expected, self.sol.findUnsortedSubarray(data))

    def test_sampleTLE(self):
        data = [0,1,2,3,4,14,52,16,51,38,18,7,44,73,40,11,35,57,32,15,43,81,9,79,37,54,22,17,10,53,29,39,82,68,77,34,70,5,13,19,50,59,49,6,21,48,65,12,47,76,75,31,71,56,69,66,62,36,61,27,8,64,33,60,45,78,58,74,28,55,30,63,20,67,24,26,42,80,46,25,23,41,72,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99]
        expected = -1 
        self.assertEqual(expected, self.sol.findUnsortedSubarray(data))

    def tearDown(self):
        self.sol = None


if __name__ == "__main__":
    unittest.main()
