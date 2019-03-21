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
    def __init__(self):
        self.ansList = []

    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        self.recursiveSum(root, sum, [])
        return self.ansList

    def recursiveSum(self, root, sum, currList):

        if root == None:
            return

        currList.append(root.val)

        if root.left == None and root.right == None:
            if root.val == sum:
                self.ansList.append( currList[:] )
            currList.pop(-1)
        else:
            self.recursiveSum(root.left, sum-root.val, currList)
            self.recursiveSum(root.right, sum-root.val, currList)
            currList.pop(-1)
            

class Unittest_hasPathSum(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        data = [5,4,8,11,None,13,4,7,2,None,None,5,1]
        root = self.createBinaryTree(data)
        expected = [ [5,4,11,2], [5,8,4,5] ]
        self.assertEqual(expected, self.sol.pathSum(root, 22))

    def tearDown(self):
        self.sol = None

    """
        There is bug here!!
    """
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
