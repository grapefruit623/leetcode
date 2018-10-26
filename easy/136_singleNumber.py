# -*- coding:utf-8 -*-
#! /usr/bin/python3
import unittest

"""
    Your algorithm should have a linear runtime
    complexity. Could you implement it without using
    extra memory?
"""
class Solution:
    """
        AC
        Using hash table, so having extra memory.
    """
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hashTable = {}

        for n in nums:
            if hashTable.get(n):
                hashTable[n] += 1
            else:
                hashTable[n] = 1

        singleNum = [ k for k in hashTable if hashTable[k] == 1 ]

        return singleNum[0]


class Unittest_singleNumber(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        data = [2,2,1]
        expectedAns = 1
        self.assertEqual(expectedAns, self.sol.singleNumber(data))

    def test_example2(self):
        data = [4,1,2,1,2]
        expectedAns = 4
        self.assertEqual(expectedAns, self.sol.singleNumber(data))

    def tearDown(self):
        self.sol = None
        
if __name__ == "__main__":
    unittest.main()

