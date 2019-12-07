# -*-coding: utf-8 -*-
#! /usr/bin/python3
import unittest

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    '''
        AC
    '''
    def partition(self, head:ListNode, x:int)->ListNode:
        if head == None:
            return None
        lowerTail = None
        higherTail = None
        root = None
        higherRoot = None

        while head != None:
            if head.val < x:
                if root == None:
                    root = lowerTail = head
                else:
                    lowerTail.next = head
                    lowerTail = head
            else:
                if higherRoot == None:
                    higherRoot = higherTail = head
                else:
                    higherTail.next = head
                    higherTail = head
            head = head.next

        if lowerTail != None:
            lowerTail.next = higherRoot
        else:
            root = higherRoot

        if higherTail != None:
            higherTail.next = None

        return root

class unittest_partition(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_sample1(self):
        head = self.createLinkedList([1,4,3,2,5,2])
        ans = self.createLinkedList([1,2,2,4,3,5])
        self.assertEqual(True, self.compareLinkedList(ans, self.sol.partition(head,3)))

    def test_sample2(self):
        head = self.createLinkedList([3,2,5,2])
        ans = self.createLinkedList([2,2,3,5])
        self.assertEqual(True, self.compareLinkedList(ans, self.sol.partition(head,3)))

    def test_sample3(self):
        head = self.createLinkedList([2,5,2,3])
        ans = self.createLinkedList([2,2,5,3])
        self.assertEqual(True, self.compareLinkedList(ans, self.sol.partition(head,3)))

    def test_sample4(self):
        head = self.createLinkedList([])
        ans = self.createLinkedList([])
        self.assertEqual(True, self.compareLinkedList(ans, self.sol.partition(head,0)))

    def test_sample5(self):
        head = self.createLinkedList([1])
        ans = self.createLinkedList([1])
        self.assertEqual(True, self.compareLinkedList(ans, self.sol.partition(head,0)))

    def compareLinkedList(self, l1, l2):
        if l1 == None and l2 == None:
            return True
        if l1 == None or l2 == None:
            return False
        while l1 != None and l2 != None:
            if l1.val != l2.val:
                return False
            else:
                l1 = l1.next
                l2 = l2.next
        return True

    def createLinkedList(self, l):
        head = None
        tail = None
        for i in l:
            if tail == None:
                head = tail = ListNode(i)
            else:
                tail.next = ListNode(i)
                tail = tail.next

        return head

if __name__ == '__main__':
    unittest.main()
