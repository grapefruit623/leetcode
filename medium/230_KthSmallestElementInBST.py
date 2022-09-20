# -*-coding: utf-8 -*-
#! /usr/bin/python3
import unittest
from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int)->int:
        return self.inOrder(root)[k-1] # zero based index

    def inOrder(self, node)->List[int]:
        if node == None:
            return []

        l = self.inOrder(node.left)
        r = self.inOrder(node.right)

        return l+[node.val]+r

class Unittest(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        root = TreeNode(3)
        root.left = TreeNode(1)
        root.right = TreeNode(4)
        root.left.right = TreeNode(2)
        k = 1
        expected = 1

        self.assertEqual(expected, self.sol.kthSmallest(root, k))
        
    def test_case2(self):
        root = TreeNode(5)
        root.right = TreeNode(6)
        
        lTree = TreeNode(3)
        lTree.right = TreeNode(4)
        lTree.left = TreeNode(2)
        lTree.left.left = TreeNode(1)

        root.left = lTree
        k = 3
        expected = 3
        
        self.assertEqual(expected, self.sol.kthSmallest(root, k))
        

if __name__ == "__main__":
    unittest.main()
