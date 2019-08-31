# -*- coding: utf-8 -*-
#! /usr/bin/python3

import unittest

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    '''
        AC
        But slowly and use extra memory.
        Time complexity O(lenA+lenB)
        Space complexity O(lenA)
    '''
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        visited = {}
        tempA = headA
        while tempA != None:
            visited[id(tempA)] = True
            tempA = tempA.next 

        tempB = headB
        while tempB != None:
            if id(tempB) in visited:
                return tempB
            tempB = tempB.next

        return None

class Unittest_getIntersectionNode(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_sample1(self):
        lA = [1,2]
        lB = [1,2,3]
        half = [1,2,3]

        headA = self.createLinkedList(lA)
        headB = self.createLinkedList(lB)
        halfList = self.createLinkedList(half)

        self.appendLinkedList(headA, halfList)
        self.appendLinkedList(headB, halfList)

        self.assertEqual( halfList, self.sol.getIntersectionNode(headA, headB))

    def test_sample2(self):
        lA = [1,2,3]
        lB = [1]
        half = [1,2]

        headA = self.createLinkedList(lA)
        headB = self.createLinkedList(lB)
        halfList = self.createLinkedList(half)

        self.appendLinkedList(headA, halfList)
        self.appendLinkedList(headB, halfList)

        self.assertEqual( halfList, self.sol.getIntersectionNode(headA, headB))
        

    def tearDown(self):
        self.sol = None

    def appendLinkedList(self, la, lb):
        while la.next != None:
            la = la.next

        la.next = lb

    def createLinkedList(self, l):
        node = None
        head = None
        for i in l:
            if (node == None):
                node = ListNode(i)
                head = node
            else:
                node.next = ListNode(i)
                node = node.next

        return head
if __name__ == "__main__":
    unittest.main()
