# -*- coding: utf-8 -*-
#! /usr/bin/python3
import unittest
from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        if preorder == []:
            return None

        if len(preorder) == 1:
            return TreeNode(preorder[0])

        node = TreeNode(preorder[0])
        i = 1
        while i < len(preorder):
            if preorder[i] < node.val:
                i += 1
            else:
                break

        node.left = self.bstFromPreorder(preorder[1:i])
        node.right = self.bstFromPreorder(preorder[i:])

        return node

if __name__ == '__main__':
    unittest.main()
