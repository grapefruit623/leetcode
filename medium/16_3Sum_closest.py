#! -*- coding: utf-8 -*-
import unittest
from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target:int)->int:
        return self.threeSumClosestThreePointer(nums, target)

    '''
        AC
    '''
    def threeSumClosestThreePointer(self, nums, target):
        nums = sorted(nums)
        length = len(nums)
        ans = float('inf')

        for i in range(length-2):
            left = i+1
            right = length-1
            while left < right:
                currentSum = nums[i] + nums[left] + nums[right] 

                if abs(currentSum-target) < abs(ans-target):
                    ans = currentSum

                if currentSum > target:
                    right -= 1
                elif currentSum < target:
                    left += 1
                else:
                    return currentSum
        return ans
    '''
        TLE
    '''
    def threeSumClosestRecursive(self, nums, target):
        self.ans = float('inf')
        nums = sorted(nums)
        self.recursive(nums, target, 0, [])
        return self.ans

    def recursive(self, nums, target, index, currentNums):
        if len(currentNums) == 3:
            currentThreeSum = sum(currentNums)
            if abs(currentThreeSum-target) < abs(self.ans-target):
                self.ans = currentThreeSum
        else:
            if index >= len(nums):
                return False

            '''
                Need to prune!!
            '''
            for i in range(index, len(nums)):
                currentNums.append(nums[i])
                self.recursive(nums, target, i+1, currentNums)
                currentNums.pop()
            return False

class Unittest(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_sample1(self):
        data = [-1,2,1,-4]
        target = 1
        expected = 2
        self.assertEqual(expected, self.sol.threeSumClosest(data, target))

    def test_sample2(self):
        data = [1,1,1,0]
        target = -100 
        expected = 2
        self.assertEqual(expected, self.sol.threeSumClosest(data, target))

    def test_sampleTLE1(self):
        data = [-7,-71,-7,-13,45,46,-50,83,-29,-72,9,32,-74,81,68,92,-31,28,-46,-86,-70,31,-62,-20,-56,97,-41,21,81,17,-14,56,69,16,25,-38,65,-48,15,16,-25,68,-41,46,-56,-2,-3,82,8,19,-32,62,92,-56,-9,43,50,100,66,-45,41,-24,-4,83,-36,79,24,97,82,89,-56,-91,75,-64,-68,96,-55,-52,-58,-37,68,27,89,-40,-42,94,-92,-70,40,74,75,-15,54,-54,0,4,-39,93,88,-31,-26,93,8,-85,-62,89,-93,98,4,-58,8,5,-93,7,30,-75,63,41,62,-52,49,93,-11,87,7,52,5,-96,-56,43,-41,-75,-16,73,6,35,-32,62,-50,-57,-25,5,-32,94,-70,6,19,-12,63,-47,76,-57,41,-49,-33,-15,-81,55,88,67,-51,100,-19,-39,62,84,-100,78,-24,31,-32,-83,33,-25,86,9,-30,-40,52,64,-30,-17,19,-69,-89,-67,-79,-100,-53]
        target = 157
        expected = 157
        self.assertEqual(expected, self.sol.threeSumClosest(data, target))

    def test_sampleWA1(self):
        data = [-55,-24,-18,-11,-7,-3,4,5,6,9,11,23,33]
        target = 0
        expected = 0
        self.assertEqual(expected, self.sol.threeSumClosest(data, target))

if __name__ == "__main__":
	unittest.main()
