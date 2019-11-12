# -*- coding: utf-8 -*-
#! /usr/bin/python
import unittest
from typing import List

class Solution:
    def search(self, nums: List[int], target: int)->int:
        return self.binarySearch(nums, 0, len(nums)-1, target)

    '''
        AC
    '''
    def binarySearch(self, nums, begin, end, target):
        if begin > end:
            return -1

        if begin == end:
            return -1 if nums[begin] != target else begin

        middle = int((begin + end)/2)

        if nums[middle] == target:
            return middle

        if nums[middle] < target:
            leftResult = -1
            rightResult = self.binarySearch(nums, middle+1, end, target)
            if nums[begin] >= nums[middle]:
                leftResult = self.binarySearch(nums, begin, middle-1, target)
        else:
            rightResult = -1
            leftResult = self.binarySearch(nums, begin, middle-1, target)
            if nums[end] <= nums[middle]:
                rightResult = self.binarySearch(nums, middle+1, end, target)
        
        if rightResult == -1 and leftResult == -1:
            return -1
        else:
            if rightResult != -1:
                return rightResult
            else:
                return leftResult

class Unittest_search(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_sample1(self):
        nums = [4,5,6,7,0,1,2]
        target = 0
        expected = 4
        self.assertEqual(expected, self.sol.search(nums, target))

    def test_sample2(self):
        nums = [4,5,6,7,0,1,2]
        target = 3
        expected = -1
        self.assertEqual(expected, self.sol.search(nums, target))

    def test_sample3(self):
        nums = [0,1,2,3,4,5,6,7]
        target = 3
        expected = 3
        self.assertEqual(expected, self.sol.search(nums, target))

    def test_sample4(self):
        nums = [1,2]
        target = 2
        expected = 1
        self.assertEqual(expected, self.sol.search(nums, target))

    def test_sample5(self):
        nums = [5,4,3,2,1]
        target = 0
        expected = -1 
        self.assertEqual(expected, self.sol.search(nums, target))

if __name__ == '__main__':
    unittest.main()
