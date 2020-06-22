import unittest
from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return self.binarySearch(nums, 0, len(nums)-1, target)
        
    def binarySearch(self, nums: List[int], i:int, j:int, target: int) -> List[int]:
        if i > j:
            return [-1,-1]

        middle = int((i+j)/2)
        
        if nums[middle] == target:
            low, higher = middle, middle
            while higher+1 <= j and nums[higher+1] == target:
                higher += 1
            while low-1 >= i and nums[low-1] == target:
                low -= 1
            return [low, higher]
            
        if nums[middle] > target:
            return self.binarySearch(nums, i, middle-1, target)
        if nums[middle] < target:
            return self.binarySearch(nums, middle+1, j, target)

class Unittest_searchRange(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_sample1(self):
        nums = [5,7,7,8,8,10]
        target = 8
        self.assertEqual([3,4], self.sol.searchRange(nums, target))

    def test_sample2(self):
        nums = [5,7,7,8,8,10]
        target = 6 
        self.assertEqual([-1,-1], self.sol.searchRange(nums, target))

if __name__ == '__main__':
    unittest.main()
