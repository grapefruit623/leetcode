# -*- coding: utf-8 -*-
from typing import List
import unittest
import heapq

class Solution:
    def maxProduct(self, nums: List[int])->int:
        ans = 0
        heapq.heapify(nums)
        maxTwoValue = heapq.nlargest(2, nums)

        return (maxTwoValue[0]-1)*(maxTwoValue[1]-1)


class Unittest(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_sample1(self):
        nums = [3,4,5,2]
        expect = 12

        self.assertEqual(expect, self.sol.maxProduct(nums))

    def test_sample2(self):
        nums = [1,5,4,5]
        expect = 16

        self.assertEqual(expect, self.sol.maxProduct(nums))

    def test_sample3(self):
        nums = [3,7]
        expect = 12

        self.assertEqual(expect, self.sol.maxProduct(nums))

if __name__ == "__main__":
    unittest.main()
