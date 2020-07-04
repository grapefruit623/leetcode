# -*- coding:utf-8 -*-
import unittest

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def minDepth(self, root:TreeNode)->int:
        self.minDepth = float('inf')
        if root == None:
            return 0
        self.dfs(root, 0)
        return self.minDepth

    def dfs(self, root, level):
        level += 1
        if root.left == None and root.right == None:
            self.minDepth = min(self.minDepth, level)
            return

        if (root.left != None):
            self.dfs(root.left, level)
        if (root.right != None):
            self.dfs(root.right, level)

class Unittest_minDepth(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_sample1(self):
        root = TreeNode(3)
        root.left = TreeNode(9)
        root.right = TreeNode(20)
        root.right.left = TreeNode(15)
        root.right.right = TreeNode(7)
        expected = 2
        self.assertEqual(expected, self.sol.minDepth(root))

    def test_sample2(self):
        root = TreeNode(3)
        expected = 1
        self.assertEqual(expected, self.sol.minDepth(root))

    def test_sample3(self):
        root = None
        expected = 0
        self.assertEqual(expected, self.sol.minDepth(root))

    def test_sample_wa1(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        expected = 2
        self.assertEqual(expected, self.sol.minDepth(root))

if __name__ == "__main__":
    unittest.main()
