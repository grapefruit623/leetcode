# -*- coding: utf-8 -*-
#! /usr/bin/python3

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        return str(self.val)

class Solution(object):
    '''
        AC
    '''
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None

        currentNode = head
        count = 0
        nodeList = []
        while currentNode:
            nodeList.append(currentNode)
            count += 1
            currentNode  = currentNode.next

        return nodeList[count/2]

        
if __name__ == "__main__":
    head = ListNode(1)
    node1 = ListNode(2)
    node2 = ListNode(3)
    node3 = ListNode(4)
    node4 = ListNode(5)
    node5 = ListNode(6)

    head.next = node1
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5


    sol = Solution()
    print (sol.middleNode(head))
