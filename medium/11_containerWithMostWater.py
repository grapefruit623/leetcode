# -*- coding: utf-8 -*-
#! /usr/bin/python3
import unittest

class Solution(object):
    """
        AC
        time complexity O(n)
        reference to Solution 2
    """
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        begin = 0
        end = len(height)-1
        maxArea = -1

        while begin < end:
            if height[begin] <= height[end]:
                maxArea = max(maxArea, height[begin]*(end-begin))
                begin += 1
            else:
                maxArea = max(maxArea, height[end]*(end-begin))
                end -= 1
        
        return maxArea

    """
        WA
    """
    def maxArea_WA(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxArea = -1
        maxHeight = -1
        maxHeightPos = 0
        waterLevel = 0
        startPos = 0
        
        for i, h in enumerate(height):
            if i == 0:
                startPos, maxHeight = i, h
                maxHeightPos = i
                waterLevel = h
            else:
                if h > maxHeight:
                    area = maxHeight*(i-maxHeightPos)
                    maxHeight = h
                    maxHeightPos = i
                elif h <= maxHeight:
                    area = h*(i-maxHeightPos)

                maxArea = maxArea if maxArea > area else area

        return maxArea
        
class Unittest_maxArea(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_increaseSample(self):
        height = [1,2,3]
        expected = 2
        self.assertEqual(expected, self.sol.maxArea(height))

    def test_decreaseSample(self):
        height = [3,2,1]
        expected = 2
        self.assertEqual(expected, self.sol.maxArea(height))

    def test_vallySample(self):
        height = [5,3,4]
        expected = 8 
        self.assertEqual(expected, self.sol.maxArea(height))

    def test_peakSample(self):
        height = [3,5,4]
        expected = 6
        self.assertEqual(expected, self.sol.maxArea(height))

    def test_sample1(self):
        height = [1,8,6,2,5,4,8,3,7]
        expected = 49
        self.assertEqual(expected, self.sol.maxArea(height))
    
    def test_shortSample(self):
        height = [1,1]
        expected = 1
        self.assertEqual(expected, self.sol.maxArea(height))

    def test_WaSample(self):
        height = [1,2,1]
        expected = 2
        self.assertEqual(expected, self.sol.maxArea(height))

if __name__ == "__main__":
    unittest.main()

