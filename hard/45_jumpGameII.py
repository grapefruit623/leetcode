# -*- coding:utf-8 -*-
import unittest
from typing import List

class Solution:
    '''
        This solution is based on my algorithm to solve jumpGameI.
        Each iteration will travel from the current position to the farthest
        and renew the farthest position in each interval.
        
        Keep track how many times to renew the farthest position. 
        When the farthest position is bigger than the last index, return count.
    '''
    def jump(self, nums:List[int])->int:
        l = len(nums)
        before = farestPos = 0
        minimumCount = 0

        while before <= farestPos:
            if farestPos >= l-1:
                break

            currFarest = farestPos 
            for i in range(before, farestPos+1):
                jumps = i + nums[i]
                currFarest = max(jumps, currFarest)
            
            before, farestPos = farestPos, currFarest
            minimumCount += 1

        return minimumCount

class unittest_jump(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_sample1(self):
        data = [2,3,1,1,4]
        expected = 2
        self.assertEqual(expected, self.sol.jump(data))

    def test_sample2(self):
        data = [2]
        expected = 0
        self.assertEqual(expected, self.sol.jump(data))

    def test_sample3(self):
        data = [1,2,3]
        expected = 2
        self.assertEqual(expected, self.sol.jump(data))

    def test_specia4(self):
        data = [1,1,1]
        expected = 2
        self.assertEqual(expected, self.sol.jump(data))

if __name__ == '__main__':
    unittest.main()
