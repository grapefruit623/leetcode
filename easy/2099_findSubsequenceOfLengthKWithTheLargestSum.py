# -*- coding: utf-8 -*-
from typing import List
import unittest
import heapq

class Solution:
    def maxSubsequence(self, nums: List[int], k: int)->List[int]:
        dataWithIndex = []
        for i in range(len(nums)):
            dataWithIndex.append( (nums[i], i) )

        dataWithIndex = sorted(dataWithIndex, key=lambda d:d[0])
        maxValueWithK = sorted(dataWithIndex[-k:],key=lambda d:d[1])

        return [ n[0] for n in maxValueWithK ]

        
class Unittest(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_sample1(self):
        nums = [2,1,3,3]
        k = 2
        expect = [3,3]
        self.assertEqual(expect, self.sol.maxSubsequence(nums, k))

    def test_sample2(self):
        nums = [-1,-2,3,4]
        k = 3
        expect = [-1,3,4]
        self.assertEqual(expect, self.sol.maxSubsequence(nums, k))

    def test_sample3(self):
        nums = [50,-75]
        k = 2
        expect = [50,-75]
        self.assertEqual(expect, self.sol.maxSubsequence(nums, k))

    def test_sample4(self):
        nums = [-56,-214,-345,952,529,-294,-325,-924,-27,-41,716,-67,-65,-481]
        k = 5
        expect = [952,529,-27,-41,716]

        self.assertEqual(expect, self.sol.maxSubsequence(nums, k))


if __name__ == "__main__":
    unittest.main()
