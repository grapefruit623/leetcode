# -*- coding: utf-8 -*-
import unittest

class Solution(object):
    '''
        AC
    '''
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """

        if nums == None or sum(nums) < s or len(nums) == 0:
            return 0

        i = 0
        numLen = len(nums)
        l = 0
        ans = float('inf')
        currentSum = 0
        while i < numLen:
            if currentSum >= s:
                ans = min(ans, l)
                currentSum -= nums[i]
                i += 1
                l = l-1 if l-1>0 else 1
            else:
                if i+l < numLen:
                    currentSum += nums[i+l]
                    l += 1
                else:
                    currentSum -= nums[i]
                    i += 1

        return ans if ans != float('inf') else 0


class Unittest_minSubArrayLen(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_sample1(self):
        nums = [2,3,1,2,4,3]
        s = 7
        expected = 2
        self.assertEqual(expected, self.sol.minSubArrayLen(s, nums))

    def test_sample2(self):
        nums = [2]
        s = 2
        expected = 1
        self.assertEqual(expected, self.sol.minSubArrayLen(s, nums))
    
    def test_sample3(self):
        s = 80
        nums = [10,5,13,4,8,4,5,11,14,9,16,10,20,8]
        expected = 6
        self.assertEqual(expected, self.sol.minSubArrayLen(s, nums))


if __name__ == '__main__':
    unittest.main()
