# -*- coding:utf-8 -*-
#! /usr/bin/python3
import unittest
from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

'''
    AC
'''
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack=[]
        ans=[]
        temp = TreeNode(-1)

        if root == None:
            return ans

        stack.append(root)

        while stack != []:
            temp = stack.pop()
            ans.append(temp.val)

            if temp.right != None:
                stack.append(temp.right)
            if temp.left != None:
                stack.append(temp.left)

        return ans

class Unittest(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        # root=[1,None,2,3]
        root=TreeNode(1)
        root.left=None
        root.right=TreeNode(2)
        root.right.left=TreeNode(3)

        expected=[1,2,3]
        self.assertEqual(expected, self.sol.preorderTraversal(root))

    def test_case2(self):
        root=None
        expected=[]
        self.assertEqual(expected, self.sol.preorderTraversal(root))

    def test_case3(self):
        # root=[1]
        root=TreeNode(1)
        expected=[1]
        self.assertEqual(expected, self.sol.preorderTraversal(root))

    def test_case4(self):
        # root=[3,1,2]
        root=TreeNode(3)
        root.left = TreeNode(1)
        root.right = TreeNode(2)

        expected=[3,1,2]
        self.assertEqual(expected, self.sol.preorderTraversal(root))

if __name__ == "__main__":
    unittest.main()
