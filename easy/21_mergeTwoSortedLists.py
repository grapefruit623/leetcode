# -*- coding: utf-8 -*-
#! /usr/bin/python3
import unittest

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

"""
    AC
    But perhaps can be modified to in-place implement.
"""
class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        temp1 = l1
        temp2 = l2
        head = None
        node = None
        smallValueNode = None

        while (temp1 != None) and (temp2 != None):
            if temp1.val <= temp2.val:
                smallValueNode = temp1
                temp1 = temp1.next
            else:
                smallValueNode = temp2
                temp2 = temp2.next

            if head == None:
                node = smallValueNode
                head = node
            else:
                node.next = smallValueNode
                node = node.next
        else:
            if temp1 == None:
                if node != None:
                    node.next = temp2
                else:
                    return temp2
            elif temp2 == None:
                if node != None:
                    node.next = temp1
                else:
                    return temp1

        return head

class UnittestMergeTwoList(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_default_sample(self):
        d1 = [1,2,4]
        l1 = self.createLinkedList(d1)
        self.verifyArrayWithLinkedList(d1, l1)
        
        d2 = [1,3,4]
        l2 = self.createLinkedList(d2)
        self.verifyArrayWithLinkedList(d2, l2)

        ans = [1,1,2,3,4,4]
        result = self.sol.mergeTwoLists(l1, l2)
        self.verifyArrayWithLinkedList(ans, result)

    def test_sample_withDiffLength(self):
        d1 = [1,2,4]
        d2 = [3,4]
        l1 = self.createLinkedList(d1)
        l2 = self.createLinkedList(d2)

        ans = [1,2,3,4,4]
        result = self.sol.mergeTwoLists(l1, l2)
        self.verifyArrayWithLinkedList(ans, result)

    def test_sample_withEmptyList(self):
        d1 = [1,2,3]
        d2 = []
        l1 = self.createLinkedList(d1)
        l2 = self.createLinkedList(d2)

        ans = [1,2,3]
        result = self.sol.mergeTwoLists(l1, l2)
        self.verifyArrayWithLinkedList(ans, result)

    def tearDown(self):
        self.sol = None
        

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
