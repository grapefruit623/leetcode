# -*- coding:utf-8 -*-
#! /usr/bin/python3
import unittest

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    """
        AC
    """
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return None

        hashTable = set()

        while head != None:
            if head in hashTable:
                return head
            hashTable.add(head)
            head = head.next
        else:
            return None

class Unittest_hasCycle(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        head = self.createLinkedList([1,2,3])
        head.next.next.next = head
        ansNode = head
        self.assertEqual(ansNode, self.sol.detectCycle(head))

    def test_example2(self):
        head = self.createLinkedList([1,2,3])
        self.assertEqual(None, self.sol.detectCycle(head))

    def test_nullexample(self):
        head = None
        self.assertEqual(None, self.sol.detectCycle(head))

    def test_example_wa1(self):
        head = self.createLinkedList([3,2,0,-4])
        """
            -4 -> 2
        """
        head.next.next.next.next = head.next
        ansNode = head.next
        self.assertEqual(ansNode, self.sol.detectCycle(head))

    def test_example_wa2(self):
        head = self.createLinkedList([-21,10,17,8,4,26,5,35,33,-7,-16,27,-12,6,29,-12,5,9,20,14,14,
                                        2,13,-24,21,23,-21,5])
        self.assertEqual(None, self.sol.detectCycle(head))

    def tearDown(self):
        self.sol = None

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
