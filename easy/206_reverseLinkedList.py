# -*- coding:utf-8 -*-
#! /usr/bin/python3
import unittest

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        return str(self.val)

"""
    AC
"""
class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        newEnd = None
        while head != None:
            temp = head.next
            head.next = newEnd
            newEnd = head
            if temp != None:
                head = temp
            else:
                break

        return head    

class Unittest_reverseList(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        l = self.createLinkedList( [1,2,3,4,5] )
        expected = [5,4,3,2,1]
        self.verifyArrayWithLinkedList(expected, self.sol.reverseList(l))

    def test_example(self):
        l = self.createLinkedList([1,2])
        expected = [2,1]
        self.verifyArrayWithLinkedList(expected, self.sol.reverseList(l))
    def tearDown(self):
        self.sol = None

    def printLinkedList(self, l):
        while l != None:
            print (l.val)
            l = l.next

    def verifyArrayWithLinkedList(self, ansArr, resultList):
        n = resultList
        for i in range(len(ansArr)):
            self.assertEqual( ansArr[i], n.val )
            n = n.next

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
