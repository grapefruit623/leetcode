# -*- coding: utf-8 -*-
#! /usr/bin/python3

import unittest

"""
    AC
    But can I implement it more fast or not lead to
    python's list structure.
"""
class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.topIndex = -1
        self.minValue = 0

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if self.topIndex == -1:
            self.minValue = x
        else:
            self.minValue = x if x < self.minValue else self.minValue

        self.stack.append(x)
        self.topIndex += 1

    def top(self):
        """
        :rtype: int
        """
        if self.topIndex >= 0:
            return self.stack[ self.topIndex ]

    def pop(self):
        """
        :rtype: void
        """
        if self.topIndex >= 0:
            self.topIndex -= 1
            p = self.stack.pop()
            if self.stack != []:
                self.minValue = min(self.stack)
        return None    

    def getMin(self):
        """
        :rtype: int
        """
        return self.minValue
        

class Unittest_minStack(unittest.TestCase):
    def setUp(self):
        self.minStack = MinStack()

    def test_top(self):
        self.minStack.push(-2)
        t = self.minStack.top()
        self.assertEqual(-2, t)

    def test_push(self):
        self.minStack.push(-2)

    def test_pop(self):
        self.minStack.push(3)
        p = self.minStack.pop()
        self.assertEqual(None, p)

    def test_getMin(self):
        self.minStack.push(-2)
        self.minStack.push(0)
        self.minStack.push(-3)
        mValue = self.minStack.getMin()
        self.assertEqual(-3, mValue)

    def test_popWithTop(self):
        self.minStack.push(-2)
        self.minStack.pop()
        self.minStack.top()

    def test_sampleWA(self):
        self.minStack.push(-2)
        self.minStack.push(0)
        self.minStack.push(-3)
        mValue = self.minStack.getMin()
        self.assertEqual(-3, mValue)

        pValue = self.minStack.pop()
        self.assertEqual(None, pValue)

        tValue = self.minStack.top()
        self.assertEqual(0, tValue)

        getValue = self.minStack.getMin()
        self.assertEqual(-2, getValue)

    def tearDown(self):
        self.minStack = None

if __name__ == "__main__":
    unittest.main()
