# -*- coding:utf-8 -*-
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
class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.depthFirstTravel(root)
    
    def depthFirstTravel(self, node):
        if (node is None) or (node.val is None):
            return 0
        else:
            leftDepth = self.depthFirstTravel(node.left)
            rightDepth = self.depthFirstTravel(node.right)

            deeper = leftDepth if leftDepth>rightDepth else rightDepth
            return deeper+1 

        

class Unittest_maxDepth(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_createBinaryTree(self):
        data = [3,9,20,None,None,15,7]
        tree = self.createBinaryTree(data)

        treeNodeQueue = [tree]
        levelOrderOutput = []

        while treeNodeQueue != []:
            n = treeNodeQueue.pop(0)
            if n is not None:
                levelOrderOutput.append(n.val)
                treeNodeQueue.append(n.left)
                treeNodeQueue.append(n.right)
        
        self.assertEqual(data, levelOrderOutput)
            
    def test_defaultSample(self):
        data = [3,9,20,None,None,15,7]
        tree = self.createBinaryTree(data)
        expectedAns = 3
        self.assertEqual(expectedAns, self.sol.maxDepth(tree))

    def test_emptyTree(self):
        data = [None]
        tree = self.createBinaryTree(data)
        expectedAns = 0
        self.assertEqual(expectedAns, self.sol.maxDepth(tree))

    def test_onlyRoot(self):
        data = [1]
        tree = self.createBinaryTree(data)
        expectedAns = 1
        self.assertEqual(expectedAns, self.sol.maxDepth(tree))

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
        
if __name__ == '__main__':
    unittest.main()
