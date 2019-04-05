#! -*- coding: utf-8 -*-
import unittest
from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        print (nums)
        if nums == [] or nums[0] > 0 or nums[-1] <0:
            return []
        
        self.ans = []
        self.len = len(nums)
        i = 0
        while i < self.len-2:
            if nums[i] > 0:
                break
                
            # To bypass duplicating number
            while (i > 0) and (i<self.len-1) and (nums[i-1] == nums[i]):
                i += 1
                
            target = 0 - nums[i]
            twoSums = self.findSubSumWithTarget(nums, i+1, target)
            for ts in twoSums:
                self.ans.append( [nums[i]] + ts)
            i += 1
        return self.ans
    
    '''
        AC
        Two pointers for twto sum to find specific target
    '''
    def findSubSumWithTarget(self, nums: List[int], index: int, target: int)->List[List[int]]:
        i = index
        j = self.len-1
        temp = []
        
        while i < j:
            if nums[i]+nums[j] < target:
                i += 1
            elif nums[i] + nums[j] > target:
                j -= 1
            else:
                temp.append( [nums[i], nums[j]])
                '''
                    Bypass duplicating combination.
                '''
                while (i < j) and (i+1<self.len) and (nums[i] == nums[i+1]):
                    i += 1
                while (i < j) and (j>0) and (nums[j-1] == nums[j]):
                    j -= 1
                i += 1
                j -= 1
        return temp
    
    '''
        Unused
        TLE
    '''                
    def findSubSum(self, nums: List[int], index: int, subSum: int, level: int, temp:List[int]):
        if level == 3:
            if subSum == 0:
                if temp not in self.ans:
                    self.ans.append(temp.copy())
        else:
            if index < self.len:
                temp.append(nums[index])
                self.findSubSum(nums, index+1, subSum - nums[index], level+1, temp)
                temp.pop(-1)
                self.findSubSum(nums, index+1, subSum, level, temp)

class Unittest(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_sample1(self):
        data = [-1,-1,2,-1,-4]
        expected = [[-1,0,1], [-1,-1,2]]
        self.assertEqual(expected, self.sol.threeSum(data))

if __name__ == "__main__":
	unittest.main()

