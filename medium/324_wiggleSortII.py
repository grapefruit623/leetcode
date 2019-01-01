# -*- coding:utf-8 -*-
#! /usr/bin/python3
import unittest

class Solution(object):
    """
        WA
    """
    def wiggleSort_wa(self, nums):
        """
        :type nums: List[int]
        :rtype void Do not return anything, modify nums in-place instead.
        """
        start = 0
        end = 0
        while start < len(nums):
            if start+1 >= len(nums):
                break
            if start % 2 == 0:
                if nums[start] > nums[start+1]:
                    nums[start], nums[start+1] = nums[start+1], nums[start]
                elif nums[start] == nums[start+1]:
                    end = start
                    while end < len(nums):
                        if nums[end] > nums[start]:
                            nums[end], nums[start+1] = nums[start+1], nums[end]
                        end += 1
            else:
                if nums[start] < nums[start+1]:
                    nums[start], nums[start+1] = nums[start+1], nums[start]
                elif nums[start] == nums[start+1]:
                    end = start
                    while end < len(nums):
                        if nums[end] < nums[start]:
                            nums[end], nums[start+1] = nums[start+1], nums[end]
                        end += 1

            start += 1

        print (nums)
        
    """
        AC
        Shorter and clearly solution
        ref: https://leetcode.com/problems/wiggle-sort-ii/discuss/77678/3-lines-Python-with-Explanation-Proof
    """
    def wiggleSort(self, nums):
        nums.sort()
        halfLen = len(nums[::2])
        nums[::2], nums[1::2] = nums[halfLen-1::-1], nums[:halfLen-1:-1]

    """
        AC
    """
    def wiggleSort_ac(self, nums):
        """
        :type nums: List[int]
        :rtype void Do not return anything, modify nums in-place instead.
        """
        sortedNums = sorted(nums)
        ans = []
        end = len(sortedNums)-1
        halfLen = int(len(sortedNums)/2)

        while end >= halfLen:
            if end != halfLen:
                ans.append(sortedNums[end-halfLen])
                ans.append(sortedNums[end])
            else:
                if len(sortedNums)%2 != 0:
                    ans.append(sortedNums[end-halfLen])
                else:
                    ans.append(sortedNums[end-halfLen])
                    ans.append(sortedNums[end])

            end -= 1

        for i in range(len(ans)):
            nums[i] = ans[i]

class Unittest_wiggleSort(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_sample2(self):
        nums = [1,3,2,2,3,1]
        self.sol.wiggleSort(nums)
        self.assertFailAns(nums)

    def test_sample(self):
        nums = [1,5,1,1,6,4]
        self.sol.wiggleSort(nums)
        self.assertFailAns(nums)

    def test_sampleWA1(self):
        nums = [1,2,2,1,2,1,1,1,1,2,2,2]
        self.sol.wiggleSort(nums)
        self.assertFailAns(nums)

    def test_sampleWA2(self):
        nums = [4,5,5,6]
        self.sol.wiggleSort(nums)
        self.assertFailAns(nums)

    def test_sampleWA3(self):
        nums = [1,2,2,1,2,1,1,1,2,2,1,2,1,2,1,1,2]
        self.sol.wiggleSort(nums)
        self.assertFailAns(nums)

    def assertFailAns(self, nums):
        numLen = len(nums)
        for i in range(numLen):
            if i % 2 == 1:
                if i-1 >=0:
                    self.assertLess(nums[i-1], nums[i]) 
                if i+1 < numLen-1:
                    self.assertGreater(nums[i], nums[i+1])
                    

if __name__ == "__main__":
    unittest.main()
