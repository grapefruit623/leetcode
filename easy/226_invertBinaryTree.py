class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __lt__(self, node):
        return self.val > node.val

    def __unicode__(self):
        return self.val

    def __str__(self):
        return str(self.val)


class Tree(object):
    def __init__(self):
        self.root = None
        self.dataSeq = []

    def __unicode__(self):
        self.dfs(self.root)
        return self.dataSeq

    def __str__(self):
        self.dfs(self.root)
        return str(self.dataSeq)

    def insert(self, x):
        newNode = TreeNode(x)
        if self.root is None:
            self.root = newNode
        else:
            node = self.root

            while node is not None:
                if node < newNode:
                    if node.left is None:
                        node.left = newNode
                        return
                    node = node.left
                else:
                    if node.right is None:
                        node.right = newNode
                        return
                    node = node.right

    def dfs(self, start):
        if start is not None:
            self.dfs(start.left)
            self.dataSeq.append(start.val)
            self.dfs(start.right)


'''
    Recursive solution 
'''
class Solution(object):
    def invertTree(self, root):
        if root is not None:
            root.left = self.invertTree(root.left)
            root.right = self.invertTree(root.right)
            temp = root.left
            root.left = root.right
            root.right = temp
            return root
        else:
            return None

if __name__ == '__main__':
    tree = Tree()
    data = [4, 2, 7, 1, 3, 6, 9]
    for i in data:
        tree.insert(i)

    print (tree)
    print ("-"*30)
    ss = Solution()
    iTree = ss.invertTree(tree.root)
    print (iTree)

