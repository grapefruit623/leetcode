# -*- coding:utf-8 -*-
#! /usr/bin/python3

import unittest

"""
    AC
"""
class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        countTable = {}
        for n in nums:
            if n in countTable.keys():
                countTable[n] += 1
            else:
                countTable[n] = 1
                    
        majorityItem = 0 
        for m in countTable.items():
            if m[1] > len(nums)/2:
                majorityItem = m

        return majorityItem[0]

class Unittest_majorityElement(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        l = [3,2,3]
        expected = 3
        self.assertEqual(expected, self.sol.majorityElement(l))

    def test_example2(self):
        l = [2,2,1,1,1,2,2]
        expected = 2
        self.assertEqual(expected, self.sol.majorityElement(l))

    def test_onlyOneData(self):
        l = [3]
        expected = 3
        self.assertEqual(expected, self.sol.majorityElement(l))

    def tearDown(self):
        self.sol = None

if __name__ == '__main__':
    unittest.main()
