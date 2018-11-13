# -*- coding: utf-8 -*-
#! /usr/bin/python3

import unittest

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

"""
    AC
"""
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if len(nums) == 0:
            return None

        if len(nums) == 1:
            return TreeNode(nums[0])

        middleLoc = int(len(nums)/2)
        root = TreeNode(nums[middleLoc])

        root.left = self.sortedArrayToBST(nums[:middleLoc])
        root.right = self.sortedArrayToBST(nums[middleLoc+1:])

        return root
        

class Unittest_sortedArrayToBST(unittest.TestCase):
    """
    :type nums: List[int]
    :rtype: TreeNode
    """
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        data = [-10, -3, 0, 5, 9]
        self.sol.sortedArrayToBST(data)

    def tearDown(self):
        self.sol = None

if __name__ == "__main__":
    unittest.main()
