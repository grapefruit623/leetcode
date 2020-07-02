#! -*- coding:utf-8 -*-
import unittest

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root:TreeNode)->bool:
        self.inOrderArr = []
        self.inOrderTraveral(root)

        for i in range(len(self.inOrderArr)-1):
            if self.inOrderArr[i] >= self.inOrderArr[i+1]:
                return False
        return True

    def inOrderTraveral(self, root):
        if root == None:
            return
        self.inOrderTraveral(root.left)
        self.inOrderArr.append(root.val)
        self.inOrderTraveral(root.right)


class Unittest_isValidBST(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_sample1(self):
        root = TreeNode(2)
        leftNode = TreeNode(1)
        rightNode = TreeNode(3)
        root.left = leftNode
        root.right = rightNode
        self.assertEqual(True, self.sol.isValidBST(root))

    def test_sample2(self):
        root = TreeNode(5)
        leftNode = TreeNode(1)
        rightNode = TreeNode(4)
        root.left = leftNode
        root.right = rightNode
        rightNode.left = TreeNode(3)
        rightNode.right = TreeNode(6)
        self.assertEqual(False, self.sol.isValidBST(root))

    def test_sample_wa1(self):
        root = TreeNode(1)
        leftNode = TreeNode(1)
        root.left = leftNode
        self.assertEqual(False, self.sol.isValidBST(root))

if __name__ == "__main__":
    unittest.main()
