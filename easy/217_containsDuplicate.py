# -*-coding:utf-8-*-
#! /usr/bin/python3
import unittest
from typing import List

'''
    AC
'''
class Solution:
    def containsDuplicate(self, nums:List[int])->bool:
        s = set()
        for n in nums:
            if n in s:
                return True
            else:
                s.add(n)
        return False
'''
    AC
'''
class Solution2:
    def containsDuplicate(self, nums:List[int])->bool:
        nums.sort()
        l = len(nums)
        for i,n in enumerate(nums):
            if i+1 < l:
                if nums[i] == nums[i+1]:
                    return True
        return False
'''
    AC
'''
class Solution3:
    def containsDuplicate(self, nums:List[int])->bool:
        if not nums:
            return False
        return len(set(nums)) != len(nums)

class Unittest(unittest.TestCase):
    def setUp(self):
        self.sol = Solution3()

    def test_sample(self):
        data = [1,2,3,1]
        expected = True
        self.assertEqual(expected, self.sol.containsDuplicate(data))

    def test_sample2(self):
        data = [1,2,3,4]
        expected = False
        self.assertEqual(expected, self.sol.containsDuplicate(data))

    def test_sample3(self):
        data = [1,1,1,3,3,4,3,2,4,2]
        expected = True
        self.assertEqual(expected, self.sol.containsDuplicate(data))

if __name__ == "__main__":
    unittest.main()
