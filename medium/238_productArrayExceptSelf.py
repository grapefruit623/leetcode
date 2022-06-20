# -*- coding: utf-8 -*-
#! /usr/bin/python3
import unittest
from typing import List

class Solution:
    '''
        O(1)
    '''
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        ans = [1]*l
        # store prefixsum at index i( prouctarray before nums[i] except nums[i]
        prefixSum = 1
        # store postsum at index i( prouctarray after nums[i] except nums[i]
        postSum = 1
        
        for i in range(1, l):
            prefixSum = nums[i-1]*prefixSum
            ans[i] = prefixSum

        for i in range(l-2, -1, -1):
            postSum = nums[i+1]*postSum
            ans[i] *= postSum

        return ans

    '''
        AC
    '''
    def productExceptSelf_ac(self, nums: List[int]) -> List[int]:
        l = len(nums)
        ans = [1]*l
        # Store prefixsum at index i( prouctArray before nums[i] except nums[i]
        prefixSum = [1]*l
        # Store postsum at index i( prouctArray after nums[i] except nums[i]
        postSum = [1]*l
        

        for i in range(1, l):
            prefixSum[i]=nums[i-1]*prefixSum[i-1]

        for i in range(l-2, -1, -1):
            postSum[i] = nums[i+1]*postSum[i+1]

        for i in range(l):
            ans[i] = prefixSum[i]*postSum[i]

        return ans

class Unittest(unittest.TestCase):
    def setUp(self):
        self.sol=Solution()

    def test_case1(self):
        nums=[1,2,3,4]
        expected=[24,12,8,6]

        self.assertEqual(expected, self.sol.productExceptSelf(nums))

    def test_case2(self):
        nums=[-1,1,0,-3,3]
        expected=[0,0,9,0,0]

        self.assertEqual(expected, self.sol.productExceptSelf(nums))

if __name__ == "__main__":
    unittest.main()
