# -*- coding: utf-8 -*-
import unittest
from typing import List

class Solution:
    def canJump(self, nums:List[int])->bool:
        if nums == []:
            return False
        return self.greedyMoveVer2(nums)

    '''
        AC
    '''
    def greedyMoveVer2(self, nums):
        canArrived = [False]*len(nums)
        canArrived[0] = True
        l = len(nums)
        i = j = 0

        while i < l and j < l:
            if i <= j:
                if canArrived[i] == True and i + nums[i] > j:
                    while j < l and j <= i+nums[i]:
                        canArrived[j] = True
                        j += 1
                    j -= 1
            else: # i > j
                '''
                    There is no way to cross jth position
                '''
                return False
            i += 1
        return canArrived[-1]
    '''
        O(n^2) solution
        TLE but better than recursive solution
    '''
    def greedyMove(self, nums):
        canArrived = [False]*len(nums)
        canArrived[0] = True
        l = len(nums)

        for i in range(l):
            for j in range(i):
                if canArrived[j] == True and j + nums[j] >= i:
                    canArrived[i] = True
                    break

        return canArrived[-1]
    '''
        Recursive solution
        TLE
    '''
    def recursiveMove(self, nums, currPos, destination)->bool:
        if currPos > destination:
            return False

        if currPos == destination:
            return True

        steps = nums[currPos]
        for i in range(1, steps+1):
            if currPos + i == destination:
                return True
            else:
                if self.recursiveMove(nums, currPos + i, destination):
                    return True
        return False


class unittest_canJump(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_sample1(self):
        data = [2,3,1,1,4]
        expected = True
        self.assertEqual(expected, self.sol.canJump(data))

    def test_sample2(self):
        data = [3,2,1,0,4]
        expected = False
        self.assertEqual(expected, self.sol.canJump(data))

    def test_sample3(self):
        data = [2]
        expected = True
        self.assertEqual(expected, self.sol.canJump(data))

    def test_sample4(self):
        data = []
        expected = False
        self.assertEqual(expected, self.sol.canJump(data))

    def test_sample5(self):
        data = [1,2,3]
        expected = True
        self.assertEqual(expected, self.sol.canJump(data))

    def test_sample6(self):
        data = [2,5,0,0]
        expected = True
        self.assertEqual(expected, self.sol.canJump(data))

    def test_sampleTLE(self):
        data = [2,0,6,9,8,4,5,0,8,9,1,2,9,6,8,8,0,6,3,1,2,2,1,2,6,
                5,3,1,2,2,6,4,2,4,3,0,0,0,3,8,2,4,0,1,2,0,1,4,6,5,
                8,0,7,9,3,4,6,6,5,8,9,3,4,3,7,0,4,9,0,9,8,4,3,0,7,
                7,1,9,1,9,4,9,0,1,9,5,7,7,1,5,8,2,8,2,6,8,2,2,7,5,1,7,9,6]
        expected = False
        self.assertEqual(expected, self.sol.canJump(data))

    def test_special(self):
        data = [0,2,3]
        expected = False
        self.assertEqual(expected, self.sol.canJump(data))

    def test_special(self):
        data = [1,1,1]
        expected = True
        self.assertEqual(expected, self.sol.canJump(data))


if __name__ == "__main__":
    unittest.main()
