# -*- coding: utf-8 -*-
#! /usr/bin/python3

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []

        queue = []
        queue.append( (root, 0) )
        return self.zigzagLevelTraversal(queue)
        
    """
       WA 
    """
    '''
    def zigzagLevelTraversal(self, queue, ans):
        if len(queue) == 0:
            return None

        while len(queue) > 0:
            (node, nodeLevel) = queue.pop(0)

            if len(ans) < nodeLevel+1:
                ans.append([])

            ans[nodeLevel].append(node.val)

            if (nodeLevel % 2 == 0):
                if node.right is not None:
                    queue.append( (node.right, nodeLevel+1) )
                if node.left is not None:
                    queue.append( (node.left, nodeLevel+1) )
            else:
                if node.left is not None:
                    queue.append( (node.left, nodeLevel+1) )
                if node.right is not None:
                    queue.append( (node.right, nodeLevel+1) )
    '''

    """
        AC
    """
    def zigzagLevelTraversal(self, queue):
        ans = []
        reuseStack = []

        while len(queue) != 0:
            (ansNode, level) = queue.pop(0)
            reuseStack.append( (ansNode, level) )

            if len(ans) < level+1:
                ans.append([])
            
            ans[level].append(ansNode.val)

            if len(queue) == 0:
                while len(reuseStack) != 0:
                    (node, nodeLevel) = reuseStack.pop()
                    if (nodeLevel % 2 == 0):
                        if node.right is not None:
                            queue.append( (node.right, nodeLevel+1) )
                        if node.left is not None:
                            queue.append( (node.left, nodeLevel+1) )
                    else:
                        if node.left is not None:
                            queue.append( (node.left, nodeLevel+1) )
                        if node.right is not None:
                            queue.append( (node.right, nodeLevel+1) )
        return ans

if __name__ == '__main__':
    """
        AC Data
    """
    '''
    root = TreeNode(3)
    root.left = TreeNode(9)
    rightSubTree = TreeNode(20)
    rightSubTree.left = TreeNode(15)
    rightSubTree.right = TreeNode(7)
    root.right = rightSubTree
    '''
    """
        WA Data
    """
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(4)
    root.right = TreeNode(3)
    root.right.right = TreeNode(5)

    sol = Solution()
    print (sol.zigzagLevelOrder(root))

