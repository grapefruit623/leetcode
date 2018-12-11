# -*- coding:utf-8 -*-
#! /usr/bin/python3
import unittest

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        return str(self.val)

class Solution(object):
    """
        AC
    """
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 == None or l2 == None:
            return l1 if l2 == None else l2

        head = tail = None
        carryNum = 0

        while l1 != None or l2 != None:
            if tail == None:
                temp = l1.val + l2.val
                carryNum = int(temp/10)
                tail = ListNode(temp%10)
                head = tail
            else:
                if l1 != None and l2 != None:
                    temp = l1.val + l2.val + carryNum
                elif l1 == None:
                    temp = l2.val + carryNum
                elif l2 == None:
                    temp = l1.val + carryNum

                carryNum = int(temp/10)
                tail.next = ListNode(temp%10)
                tail = tail.next

            if l1 != None:
                l1 = l1.next
            if l2 != None:
                l2 = l2.next

        if carryNum != 0:
            tail.next = ListNode(carryNum)

        return head

class Unittest_addTwoNumbers(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_sample1(self):
        l1 = self.createLinkedList([2,4,3])
        l2 = self.createLinkedList([5,6,4])
        expected = [7,0,8]
        self.verifyArrayWithLinkedList(expected, self.sol.addTwoNumbers(l1, l2))

    def test_sample2(self):
        l1 = self.createLinkedList([2,4])
        l2 = self.createLinkedList([5,6,4])
        expected = [7,0,5]
        self.verifyArrayWithLinkedList(expected, self.sol.addTwoNumbers(l1, l2))

    def test_sample3(self):
        l1 = self.createLinkedList([2,4])
        l2 = self.createLinkedList([5,6,9])
        expected = [7,0,0,1]
        self.verifyArrayWithLinkedList(expected, self.sol.addTwoNumbers(l1, l2))

    def test_sample4(self):
        l1 = self.createLinkedList([])
        l2 = self.createLinkedList([])
        expected = []
        self.verifyArrayWithLinkedList(expected, self.sol.addTwoNumbers(l1, l2))

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
