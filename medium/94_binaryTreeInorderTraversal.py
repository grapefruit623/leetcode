# -*- coding: utf-8 -*-
import unittest
from typing import List

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    '''
        AC
        Iterative solution
    '''
    def Iterative_inorderTraversal(self, root: TreeNode)->List[int]:
        ans = []
        stack = []
        
        if root == None:
            return ans

        stack.append(root)

        while stack != []:
            top = stack.pop()
            if top.left == None and top.right == None:
                ans.append(top.val)
            else:
                if top.right != None:
                    stack.append(top.right)

                stack.append(top)

                if top.left != None:
                    stack.append(top.left)

                top.right = top.left = None

        return ans

class Unittest_inorderTraversal(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_sample1(self):
        root = TreeNode(1)
        rightNode = TreeNode(2)
        rightNode.left = TreeNode(3)
        root.right = rightNode
        self.assertEqual([1,3,2], self.sol.Iterative_inorderTraversal(root))

    def test_sample2(self):
        root = None
        self.assertEqual([], self.sol.Iterative_inorderTraversal(root))

    def test_sample3(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)

        lrTree = TreeNode(5)
        lrTree.left = TreeNode(7)
        lrTree.right = TreeNode(8)

        root.left.right = lrTree

        rlTree = TreeNode(6)
        rlTree.right = TreeNode(9)

        root.right.left = rlTree
        self.assertEqual([4,2,7,5,8,1,6,9,3], self.sol.Iterative_inorderTraversal(root))
    
if __name__ == '__main__':
    unittest.main()
