# -*- coding:utf-8 -*-
#! /usr/bin/python3
import unittest

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    """
        Two pointer
        AC
    """
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slowPointer = head
        fastPointer = head

        while slowPointer != None and fastPointer != None:
            slowPointer = slowPointer.next
            if fastPointer.next != None and fastPointer.next.next != None:
                fastPointer = fastPointer.next.next
            else:
                return False

            if slowPointer == fastPointer:
                return True
        else:
            return False

    """
        AC
    """
    def hasCycleV1(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == None:
            return False

        hashTable = set()

        while head != None:
            if head in hashTable:
                return True
            hashTable.add(head)
            head = head.next
        else:
            return False

class Unittest_hasCycle(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        head = self.createLinkedList([1,2,3])
        head.next.next.next = head
        self.assertEqual(True, self.sol.hasCycle(head))

    def test_example2(self):
        head = self.createLinkedList([1,2,3])
        self.assertEqual(False, self.sol.hasCycle(head))

    def test_nullexample(self):
        head = None
        self.assertEqual(False, self.sol.hasCycle(head))

    def test_example_wa1(self):
        head = self.createLinkedList([3,2,0,-4])
        """
            -4 -> 2
        """
        head.next.next.next.next = head.next
        self.assertEqual(True, self.sol.hasCycle(head))

    def test_example_wa2(self):
        head = self.createLinkedList([-21,10,17,8,4,26,5,35,33,-7,-16,27,-12,6,29,-12,5,9,20,14,14,
                                        2,13,-24,21,23,-21,5])
        self.assertEqual(False, self.sol.hasCycle(head))

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
