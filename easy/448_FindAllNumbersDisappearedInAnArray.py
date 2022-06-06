# -*- coding: utf-8 -*-
#! /usr/bin/python3
import unittest
from typing import List

class Solution:
    '''
        AC
        ref: https://blog.csdn.net/qq_37821701/article/details/103867624
    '''
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        l = len(nums)
        for i in range(l):
            index=abs(nums[i])-1
            if nums[index] > 0:
                nums[index] = -1*nums[index]

        ans=[]
        for i in range(1, l+1):
            if nums[i-1] > 0:
                ans.append(i)

        return ans

class Unittest(unittest.TestCase):
    def setUp(self):
        self.sol=Solution()

    def test_case1(self):
         nums=[4,3,2,7,8,2,3,1]
         expect=[5,6]

         self.assertEqual(expect, self.sol.findDisappearedNumbers(nums))

if __name__ == "__main__":
    unittest.main()


