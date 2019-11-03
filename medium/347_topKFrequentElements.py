# -*- coding: utf-8 -*-
#! /usr/bin/python3
import unittest
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int)->List[int]:
        heap = {}
        for n in nums:
            if n in heap:
                heap[n] += 1
            else:
                heap[n] = 1

        sResult = sorted(heap.items(), key=lambda x:x[1])
        return  [ s[0] for s in sResult[-1:-1-k:-1] ]

class Unittest_topKFrequent(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_sample1(self):
        inp = [1,1,1,2,2,3]
        k = 2
        expected = [1,2]
        self.assertEqual(self.sol.topKFrequent(inp, k), expected)

    def test_sample2(self):
        inp = [1]
        k = 1
        expected = [1]
        self.assertEqual(self.sol.topKFrequent(inp, k), expected)

if __name__ == '__main__':
    unittest.main()
