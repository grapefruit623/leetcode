#! -*- coding:utf-8 -*-
#! /usr/bin/python3
import unittest
from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return None

        '''
            What is definition of dp array?
            dp_max[i] is the maximum value which contains nums[i]
            dp_min[i] is the minimum value which contains nums[i]
        '''
        dp_min = []
        dp_max = []
        dp_min.append(nums[0])
        dp_max.append(nums[0])

        for i,n in enumerate(nums):
            if i > 0:
                '''
                    if dp_min[i-1] is (-) and nums[i] is (-)
                        then dp_min[i-1]*nums[i] will be dp_max[i]
                    
                    if dp_max[i-1] and nums[i] are different minus
                        then will their multiple be dp_min[i]
                '''
                dp_max.append(max(nums[i], nums[i]*dp_max[i-1], nums[i]*dp_min[i-1]))
                dp_min.append(min(nums[i], nums[i]*dp_max[i-1], nums[i]*dp_min[i-1]))
                    
        return max(dp_max)


class unittest_maxProduct(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_sample1(self):
        data = [2,3,-2,4]
        expected = 6
        print ('data: ', data)
        self.assertEqual(expected, self.sol.maxProduct(data))

    def test_sample2(self):
        data = [-2,3,-2,4]
        expected = 48 
        print ('data: ', data)
        self.assertEqual(expected, self.sol.maxProduct(data))

    def test_sample3(self):
        data = [2,-3,4]
        expected = 4 
        print ('data: ', data)
        self.assertEqual(expected, self.sol.maxProduct(data))

    def test_sample4(self):
        data = [-2,0,-1]
        expected = 0 
        print ('data: ', data)
        self.assertEqual(expected, self.sol.maxProduct(data))

if __name__ == "__main__":
    unittest.main()
