# -*- coding: utf-8 -*-
#! /usr/bin/python3
import unittest

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.val)

"""
    AC
"""
class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root == None:
            return False

        if root.left == None and root.right == None:
            if root.val == sum:
                return True
            else:
                return False
        else:
            l = self.hasPathSum(root.left, sum-root.val)
            r = self.hasPathSum(root.right, sum-root.val)
            return l or r
            

class Unittest_hasPathSum(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        data = [5,4,8,11,None,13,4,7,2,None,None,None,1]
        root = self.createBinaryTree(data)
        self.assertEqual(True, self.sol.hasPathSum(root, 22))

    def tearDown(self):
        self.sol = None

    def createBinaryTree(self, data):
        if data is []:
            return None

        j = 0
        node = None
        dataLen = len(data)
        root = TreeNode(data[0])
        treeNodeList = [ root ]
        test = []

        while treeNodeList != []:
            node = treeNodeList.pop(0)
            test.append(node)
            if node.val is not None:
                if (2*j + 1) < dataLen:
                    node.left = TreeNode(data[2*j+1])
                    treeNodeList.append(node.left)

                if (2*j+2) < dataLen:
                    node.right = TreeNode(data[2*j+2])
                    treeNodeList.append(node.right)

            j += 1

        return root

if __name__ == "__main__":
    unittest.main()
