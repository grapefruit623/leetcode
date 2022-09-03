# -*- coding:utf-8 -*-
#! /usr/bin/python3
import unittest
from typing import List
import unittest

class Solution:
    def minimumOperations(self, nums: List[int])->int:
        '''
            priority queue
        '''
        ans = 0
        nums = sorted(nums)

        while nums != []:
            minValue = nums.pop(0)

            if minValue == 0:
                continue
            
            for i in range(len(nums)):
                nums[i] -= minValue

            for n in nums:
                if n == 0:
                    nums.pop(0)
                else:
                    break

            ans += 1

        return ans

class unittest_isPalindrome(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_sampel1(self):
        nums = [1,5,0,3,5]
        expect = 3
        self.assertEqual(expect, self.sol.minimumOperations(nums))

    def test_sampel2(self):
        nums = [0]
        expect = 0
        self.assertEqual(expect, self.sol.minimumOperations(nums))

    def test_sampel3(self):
        nums = [0,0,0,0]
        expect = 0
        self.assertEqual(expect, self.sol.minimumOperations(nums))

if __name__ == '__main__':
    unittest.main()
