# -*- coding: utf-8 -*-
#! /usr/bin/python3
import unittest

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

"""
    AC
"""
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        linkedListLen = self.calculateLinkedListLength(head)

        if linkedListLen == 1 or linkedListLen == 0:
            return True

        """
            Move node pointer to half linked list
        """
        untilHalfLen = linkedListLen/2
        untilHalfHead = None

        while untilHalfLen > 0:
            untilHalfLen -= 1
            if untilHalfHead == None:
                untilHalfHead = head
            else:
                untilHalfHead = untilHalfHead.next

        """
            Split linked list to two parts.
        """
        temp = untilHalfHead.next
        untilHalfHead.next = None
        untilHalfHead = temp

        """
            Reverse later half list.
        """
        reverseHalfHead = self.reverseList(untilHalfHead)

        """
            Compare two linked list.
        """
        while head != None and reverseHalfHead != None:
            if head.val != reverseHalfHead.val:
                return False

            head = head.next
            reverseHalfHead = reverseHalfHead.next
       
        return True

    def calculateLinkedListLength(self, head):
        linkedListLen = 0

        while head != None:
            linkedListLen += 1
            head = head.next

        return linkedListLen

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

class Unittest_isPalindrome(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        l = [1,2]
        head = self.createLinkedList(l)
        self.assertEqual(False, self.sol.isPalindrome(head))

    def test_example2(self):
        l = [1,2,2,1]
        head = self.createLinkedList(l)
        self.assertEqual(True, self.sol.isPalindrome(head))

    def test_empty(self):
        l = []
        head = self.createLinkedList(l)
        self.assertEqual(True, self.sol.isPalindrome(head))

    def test_oneElement(self):
        l = [1]
        head = self.createLinkedList(l)
        self.assertEqual(True, self.sol.isPalindrome(head))

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
